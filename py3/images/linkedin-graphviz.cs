#!/usr/bin/env python

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/auth/bxRepos/bisos-pip/binsprep/py3/bin/exmpl-func-binsPrep.cs
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

""" #+begin_org
* Panel::  [[file:/bisos/panels/bisos-apps/lcnt/lcntScreencasting/subTitles/_nodeBase_/fullUsagePanel-en.org]]
* Overview and Relevant Pointers
#+end_org """

from bisos import b
from bisos.b import cs

import graphviz
import typing

from bisos.graphviz import graphvizSeed
ng = graphvizSeed.namedGraph

######  NOTYET (Begin)
STYLE: dict = {
    "edgeColors": {
        "generate": "darkgreen",
        "link": "blue",
        "enrich": "red"
    },
    "nodes": {
        "ExportedData": {"label": "LinkedIn Exported Zip", "shape": "box", "style": "filled", "fillcolor": "#e0e0e0"},
        "ConnectionsCSV": {"label": "Connections.csv", "shape": "note"},
        "ProfileCSV": {"label": "Profile.csv", "shape": "note"},
        "MessagesCSV": {"label": "Messages.csv", "shape": "note"},
        "BaseVCard": {"label": "Base VCard (Raw Connections)", "shape": "ellipse", "style": "filled", "fillcolor": "#d0f0c0"},
        "WebCons": {"label": "Web Contacts", "shape": "ellipse", "style": "filled", "fillcolor": "#c0d0f0"},
        "ExternalContacts": {"label": "External Contacts", "shape": "ellipse", "style": "filled", "fillcolor": "#f0c0c0"},
        "EnrichedVCard": {"label": "Enriched VCard", "shape": "ellipse", "style": "filled", "fillcolor": "#f8e0b0"},
    },
    "legend": [
        ("Legend1", "🟢 Green: Raw Conversion"),
        ("Legend2", "🔵 Blue: Local Linking"),
        ("Legend3", "🔴 Red: External Enrichment"),
    ]
}


def nodeApply(dot: graphviz.Digraph, name: str) -> None:
    """Apply styling from STYLE dict and add the node to the graph."""
    attrs: dict = STYLE["nodes"].get(name, {})
    dot.node(name, **attrs)
#######  NOTYET (End)

def nodeVCard(dot: graphviz.Digraph) -> None:
    dot.node('VCard', "LinkedIn\nVCard",  shape='box', style='filled', fillcolor='gray95')

def nodeVCardPlus(dot: graphviz.Digraph) -> None:
    dot.node('VCardPlus', "Plus\nLinkedIn\nVCard", shape='box', style='filled', fillcolor='gray85')


####+BEGIN: b:py3:cs:func/typing :funcName "exportedFileInfo" :funcType "Typed" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-Typed  [[elisp:(outline-show-subtree+toggle)][||]] /exportedFileInfo/  deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def exportedFileInfo(
####+END:
        asRoot: bool=True,
) -> graphviz.Digraph:
    """ #+begin_org
    ** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    if asRoot == False:
        raise ValueError("exportedFileInfo must be called with asRoot=True")

    # Create a new directed graph
    dot = graphviz.Digraph(comment='LinkedIn vCard Data Flow - Extended')

    # LinkedIn core node group
    with dot.subgraph(name='cluster_linkedin') as c:
        c.attr(label='www.LinkedIn.com', color='lightblue')
        c.node('LinkedIn', style='filled', fillcolor='lightblue2')

    # LinkedIn Exported Info group
    with dot.subgraph(name='cluster_exported') as c:
        c.attr(label='LinkedIn Exported Info', color='lightblue')
        c.node('Export.zip', style='filled', fillcolor='lightblue')
        c.node('ExportedData', style='filled', fillcolor='lightblue')
        c.node('Connections.csv', style='filled', fillcolor='lightblue')
        c.node('Invitations.csv', style='filled', fillcolor='lightblue')
        c.node('Messages.csv', style='filled', fillcolor='lightblue')
        c.edge('Export.zip', 'ExportedData', label='unzip')
        c.edge('ExportedData', 'Connections.csv')
        c.edge('ExportedData', 'Invitations.csv')
        c.edge('ExportedData', 'Messages.csv')

    # Cross-group edges
    dot.edge('LinkedIn', 'Export.zip', label='LinkedInExportProcess', color='blue')

    # Central VCard nodes with distinct style
    # dot.node('VCard', "LinkedIn\nVCard",  shape='box', style='filled', fillcolor='gray95')
    nodeVCard(dot)

    # Data flow to VCard
    dot.edge('Connections.csv', 'VCard', label='generate')
    dot.edge('Invitations.csv', 'VCard', label='augment')
    dot.edge('Messages.csv', 'VCard', label='augment')

    return dot

####+BEGIN: b:py3:cs:func/typing :funcName "exportedPlusWebCons" :funcType "Typed" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-Typed  [[elisp:(outline-show-subtree+toggle)][||]] /exportedPlusWebCons/  deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def exportedPlusWebCons(
####+END:
       asRoot: bool=False,
) -> graphviz.Digraph:
    """ #+begin_org
    ** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    if asRoot == True:
        print(f"EH_badUsage")
        return None

    dot = exportedFileInfo()  # Get the base LinkedIn vCard graph

    # LinkedIn Web Info group
    with dot.subgraph(name='cluster_web') as c:
        c.attr(label='LinkedIn Web Info', color='lightblue')
        c.node('ContactInfo', style='filled', fillcolor='lightskyblue')

    # Cross-group edges
    dot.edge('LinkedIn', 'ContactInfo', label='WebAccess', color='blue')

    # Data flow to VCard
    dot.edge('ContactInfo', 'VCard', label='enrich', color='darkblue')

    return dot


####+BEGIN: b:py3:cs:func/typing :funcName "exportedPlusWebConsPlusExternal" :funcType "Typed" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-Typed  [[elisp:(outline-show-subtree+toggle)][||]] /exportedPlusWebConsPlusExternal/  deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def exportedPlusWebConsPlusExternal(
####+END:
       asRoot: bool=False,
) -> graphviz.Digraph:
    """ #+begin_org
    ** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    if asRoot == True:
        print(f"EH_badUsage")
        return None

    dot = exportedPlusWebCons()  # Get the base LinkedIn vCard graph

    # External sources group
    with dot.subgraph(name='cluster_external') as c:
        c.attr(
            label='External Sources',
            style='filled',
            color='orange',
            fillcolor='linen'  # light background fill
        )
        c.node('External', "Web Info", style='filled', fillcolor='mistyrose')
        c.node('ExtAddrBook', "Address\nBook",style='filled', fillcolor='mistyrose')
        c.node('ExtTags', "Tags\nGroupings",style='filled', fillcolor='mistyrose')
        c.node('ExternalInfo', style='filled', fillcolor='mistyrose')
        c.edge('External', 'ExternalInfo',  color='orangered')
        c.edge('ExtAddrBook', 'ExternalInfo', color='orangered')
        c.edge('ExtTags', 'ExternalInfo', color='orangered')

    # Central VCard nodes with distinct style
    # dot.node('VCardPlus', "Plus\nLinkedIn\nVCard", shape='box', style='filled', fillcolor='gray85')
    nodeVCardPlus(dot)

    # Data flow to VCard
    dot.edge('ExternalInfo', 'VCardPlus', color='red')
    dot.edge('VCardPlus', 'VCard', label='Cross Ref', dir='both', style='dashed', color='darkgreen')

    return dot

####+BEGIN: b:py3:cs:func/typing :funcName "linkedinVcardWithConsumers" :funcType "Typed" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-Typed  [[elisp:(outline-show-subtree+toggle)][||]] /linkedinVcardWithConsumers/  deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def linkedinVcardWithConsumers(
####+END:
       asRoot: bool=False,
) -> graphviz.Digraph:
    """ #+begin_org
    ** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    """Extended diagram: includes address book consumers for both
    VCard and VCardPlus outputs.
    """

    if asRoot == True:
        dot = graphviz.Digraph(comment='LinkedIn vCard Data Flow - Extended')
        nodeVCard(dot)
        nodeVCardPlus(dot)
    else:
        dot = exportedPlusWebConsPlusExternal()

    # Address Book Consumers group
    with dot.subgraph(name='cluster_consumers') as c:
        c.attr(label='Address Book Consumers', style='filled', color='green', fillcolor='lightgreen')
        c.node('Outlook', style='filled', fillcolor='palegreen')
        c.node('GoogleContacts', label='Google Contacts', style='filled', fillcolor='palegreen')
        c.node('AppleContacts', label='Apple Contacts', style='filled', fillcolor='palegreen')
        c.node('ebdb', label='Emacs EBDB', style='filled', fillcolor='palegreen')

    # VCard and VCardPlus to consumers
    for contact_app in ['Outlook', 'GoogleContacts', 'AppleContacts', 'ebdb']:
        # dot.edge('VCard', contact_app, label='import')
        dot.edge('VCard', contact_app,)
        dot.edge('VCardPlus', contact_app, color='red')

    return dot


def linkedinVcardWithConsumersRoot(): return linkedinVcardWithConsumers(asRoot=True)

####+BEGIN: b:py3:cs:func/typing :funcName "ebdbMtdt" :funcType "Typed" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-Typed  [[elisp:(outline-show-subtree+toggle)][||]] /ebdbMtdt/  deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def ebdbMtdt(
####+END:
       asRoot: bool=False,
) -> graphviz.Digraph:
    """ #+begin_org
    ** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    """Builds on linkedinVcardWithConsumers and adds MTDT layer."""

    if asRoot == True:
        dot = linkedinVcardWithConsumersRoot()
    else:
        dot = linkedinVcardWithConsumers()

    # Add MTDT subgroup (based on EBDB)
    with dot.subgraph(name='cluster_mtdt') as c:
        c.attr(label='MTDT: Mail Templating Distribution & Tracking',
               style='filled', color='lightgoldenrod1')

        c.node('mtdt-names', style='filled', fillcolor='yellow')
        c.node('mtdt-addressBook', style='filled', fillcolor='yellow')
        c.node('mtdt-distribution', style='filled', fillcolor='yellow')
        c.node('mtdt-mailings', style='filled', fillcolor='yellow')

        # Edges from EBDB to MTDT components with non-black color
        c.edge('ebdb', 'mtdt-names', color='darkgreen')
        c.edge('ebdb', 'mtdt-addressBook', color='darkgreen')
        c.edge('ebdb', 'mtdt-distribution', color='darkgreen')
        c.edge('ebdb', 'mtdt-mailings', color='darkgreen')

    return dot

def ebdbMtdtRoot(): return ebdbMtdt(asRoot=True)


####+BEGIN: b:py3:cs:orgItem/basic :type "=Seed Setup= " :title "*Common Facilities*" :comment "General"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Seed Setup=  [[elisp:(outline-show-subtree+toggle)][||]] *Common Facilities* General  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

namedGraphsList: typing.List[typing.Tuple[str, typing.Callable[[], graphviz.Digraph]]]  = [
    ng("exportedFileInfo", func=exportedFileInfo),
    ng("exportedPlusWebCons", func=exportedPlusWebCons),
    ng("exportedPlusWebConsPlusExternal", func=exportedPlusWebConsPlusExternal),
    ng("linkedinVcardWithConsumers", func=linkedinVcardWithConsumers),
    ng("linkedinVcardWithConsumersRoot", func=linkedinVcardWithConsumersRoot),
    ng("ebdbMtdt", func=ebdbMtdt),
    ng("ebdbMtdtRoot", func=ebdbMtdtRoot),
]

graphvizSeed.setup(
    seedType="common",
    namedGraphsList=namedGraphsList,
    # examplesHook=qmail_binsPrep.examples_csu,
)

