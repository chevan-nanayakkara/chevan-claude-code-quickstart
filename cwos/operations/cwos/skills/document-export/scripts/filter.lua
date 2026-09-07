-- Maps a design-document export's semantic HTML onto the brand styles in
-- reference.docx, and strips every element identifier so pandoc emits no
-- heading bookmarks (Google Docs renders those as stray bookmark markers).
--
--   pandoc content.html -f html -t docx --reference-doc=reference.docx \
--     --lua-filter=filter.lua -o out.docx

local EN_SPACE = pandoc.Str("\u{2002}")

local function strip_id(el)
  el.identifier = ""
  return el
end

-- Any element carrying an identifier becomes a w:bookmarkStart.
Table = strip_id
Figure = strip_id
Cell = strip_id
Row = strip_id
CodeBlock = strip_id
Code = strip_id
Link = strip_id
Image = strip_id

function Header(el)
  el.identifier = ""
  -- a leading <span> is the section number ("5" in "5 The Buildings"); the gap
  -- after it was a CSS margin, which has no equivalent in a Word run
  if el.content[1] and el.content[1].t == "Span" then
    local sp = el.content[1]
    sp.identifier = ""
    sp.attributes["custom-style"] = "NumberMark"
    if el.content[2] and el.content[2].t ~= "Space" then
      table.insert(el.content, 2, EN_SPACE)
    end
  end
  return el
end

-- Promote a leading label run ("ESTIMATE", "NOTE") to the accent character style.
local function label_first_run(blocks)
  local first = blocks[1]
  if first and (first.t == "Para" or first.t == "Plain") then
    local inl = first.content
    if inl[1] and inl[1].t == "Strong" then
      inl[1] = pandoc.Span(inl[1].content, { ["custom-style"] = "CalloutLabel" })
      if inl[2] and inl[2].t ~= "Space" then
        table.insert(inl, 2, EN_SPACE)
      end
    end
  end
  return blocks
end

-- Decoration-only wrappers (1px flex separators and the like) would otherwise
-- become empty paragraphs.
local function is_empty(blocks)
  for _, b in ipairs(blocks) do
    if b.t ~= "Null" then
      if pandoc.utils.stringify(b):gsub("%s", "") ~= "" or b.t == "Figure" or b.t == "Table" then
        return false
      end
      local has_image = false
      pandoc.walk_block(b, { Image = function() has_image = true end })
      if has_image then return false end
    end
  end
  return true
end

function Div(el)
  el.identifier = ""
  local style = el.attributes["style"] or ""

  if el.classes:includes("aside") then
    el.attributes["custom-style"] = "Callout"
    el.content = label_first_run(el.content)
  elseif style:find("color: var%(%-%-color%-coral%)") and style:find("uppercase") then
    el.attributes["custom-style"] = "Label"       -- accent-colored label
  elseif style:find("color: var%(%-%-text%-60%)") and style:find("uppercase") then
    el.attributes["custom-style"] = "LabelMuted"  -- muted label ("Contents")
  elseif is_empty(el.content) then
    return {}
  end

  el.attributes["style"] = nil
  return el
end

function BlockQuote(el)
  el.content = label_first_run(el.content)
  return el
end

function Span(el)
  el.identifier = ""
  el.attributes["style"] = nil
  return el
end

function Para(el)
  if #el.content == 0 then return {} end
  return el
end
