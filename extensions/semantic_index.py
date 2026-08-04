"""Semantic inline roles that add exact-location entries to Sphinx's index."""

from __future__ import annotations

from docutils import nodes
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole


class _IndexedRole(SphinxRole):
    """Base role that emits an index entry, an anchor, and visible text."""

    node_class: type[nodes.TextElement]

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        target_id = f"index-{self.env.new_serialno('semantic-index')}"
        entry = self.text.strip()

        index_node = addnodes.index(
            entries=[("single", entry, target_id, "", None)]
        )
        target_node = nodes.target("", "", ids=[target_id])
        self.inliner.document.note_explicit_target(target_node)
        visible_node = self.node_class(self.rawtext, entry)

        for node in (index_node, target_node, visible_node):
            self.set_source_info(node)

        return [index_node, target_node, visible_node], []


class ConceptRole(_IndexedRole):
    """Display an indexed pedagogical concept in bold."""

    node_class = nodes.strong


class FunctionRole(_IndexedRole):
    """Display an indexed Python function name as inline code."""

    node_class = nodes.literal


def setup(app: Sphinx) -> dict[str, object]:
    app.add_role("concept", ConceptRole())
    app.add_role("funcindex", FunctionRole())
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

