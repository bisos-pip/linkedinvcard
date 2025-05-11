# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= as equivalent of facter in py and remotely with rpyc.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/myLinkedIn/py3/bisos/myLinkedIn/linkedin_csu.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/myLinkedIn/py3/bisos/myLinkedIn/linkedin_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['linkedin_csu'], }
csInfo['version'] = '202505100819'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'linkedin_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
This a =Cs-Unit= for running the equivalent of facter in py and remotely with rpyc.
With BISOS, it is used in CMDB remotely.

** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= "  :title "*Py Library IMPORTS*" :comment "-- Framework and External Packages Imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- Framework and External Packages Imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# import os
import collections
# import pathlib
# import invoke

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] *Imports* =Based on Classification=cs-u=
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

# from bisos.facter import facter
# from bisos.banna import bannaPortNu

import pathlib
import re

# from telemetry import Telemetry

from bisos.myLinkedIn import utils
from bisos.myLinkedIn import connections
from bisos.myLinkedIn import invitations
from bisos.myLinkedIn import messages

from bisos.myLinkedIn import messages_822

####+BEGIN: b:py3:cs:orgItem/basic :type "=Executes=  "  :title "CSU-Lib Executions" :comment "-- cs.invOutcomeReportControl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Executes=   [[elisp:(outline-show-subtree+toggle)][||]] CSU-Lib Executions -- cs.invOutcomeReportControl  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

cs.invOutcomeReportControl(cmnd=True, ro=True)

####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    csParams.parDictAdd(
        parName='vcardsDir',
        parDescription="Path to the directory where .vcf files are stored or will be written.",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--vcardsDir',
    )
    csParams.parDictAdd(
        parName='myLinkedInBase',
        parDescription="Path to the directory where myLinkedIn files and directories are stored or will be written.",
        parDataType=None,
        parDefault="~/bpos/usageEnvs/selected/linkedin",
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--myLinkedInBase',
    )
    csParams.parDictAdd(
        parName='linCsv',
        parDescription="Specify the LinkedIn CSV file to process from the export.",
        parDataType=None,
        parDefault="Connections.csv",
        parChoices=["Connections.csv", "Invitations.csv", "Messages.csv"],
        argparseShortOpt=None,
        argparseLongOpt='--linCsv',
    )

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Direct Command Services" :anchor ""  :extraInfo "Examples and CSs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Direct Command Services_: |]]  Examples and CSs  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_csu>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        cs.examples.menuChapter('=Direct Interface Commands=')

        fileName = "/tmp/facterFile.json"

        perfNamePars = od([('perfName', "HSS-1012"),])
        fromFilePars = od([('fromFile', fileName), ('cache', 'True')])
        fromFilePlusPerfNamePars = od(list(perfNamePars.items()) + list(fromFilePars.items()))

        # cmnd('facterJsonOutputBytesToFile', pars=od([('perfName', "HSS-1012"), ('fromFile', fileName)]),)

        cs.examples.menuSection('/Export Base /')

        cmnd('exportedPrep',  args='''~/bpos/usageEnvs/selected/linkedin/Basic_LinkedInDataExport-selected.zip''')

        cs.examples.menuSection('/Generate Initial VCards/')

        cmnd('vcardsGenerate',
             pars=od([('vcardsDir', '~/bpos/usageEnvs/selected/linkedin/LinkedInVcards-selected'),]),
             args='''~/bpos/usageEnvs/selected/linkedin/LinkedInDataExport_selected/Connections.csv''')

        cs.examples.menuSection('/Augment VCards/')

        cmnd('vcardsInvitations',
             pars=od([('vcardsDir', '~/bpos/usageEnvs/selected/linkedin/LinkedInVcards-selected'),]),
             args='''~/bpos/usageEnvs/selected/linkedin/LinkedInDataExport_selected/Invitations.csv''')

        cmnd('vcardsMessages',
             pars=od([('vcardsDir', '~/bpos/usageEnvs/selected/linkedin/LinkedInVcards-selected'),]),
             args='''~/bpos/usageEnvs/selected/linkedin/LinkedInDataExport_selected/messages.csv''')


        return(cmndOutcome)


def extract_date_from_filename(zip_path: pathlib.Path) -> str:
    """Extracts the date portion (MM-DD-YYYY) from a LinkedIn ZIP filename."""
    match = re.search(r'LinkedInDataExport_(\d{2}-\d{2}-\d{4})', zip_path.name)
    if match:
        return match.group(1)
    raise ValueError(f"Date not found in filename: {zip_path.name}")



def refresh_symlink_dir(symlink_path: pathlib.Path, target_dir: pathlib.Path) -> None:
    """
    Replace or create a symbolic link pointing to target_dir.

    Args:
        symlink_path (Path): The path where the symlink will be created.
        target_dir (Path): The directory the symlink should point to.
    """
    symlink_path = symlink_path.expanduser()
    target_dir = target_dir.expanduser().resolve(strict=True)

    if symlink_path.exists() or symlink_path.is_symlink():
        symlink_path.unlink()

    symlink_path.symlink_to(target_dir, target_is_directory=True)
    print(f"Symlink refreshed: {symlink_path} → {target_dir}")

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "exportedPrep" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "myLinkedInBase" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<exportedPrep>>  =verify= parsOpt=myLinkedInBase argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class exportedPrep(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'myLinkedInBase', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             myLinkedInBase: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'myLinkedInBase': myLinkedInBase, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        myLinkedInBase = csParam.mappedValue('myLinkedInBase', myLinkedInBase)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns runFacterAndGetJsonOutputBytes.
        #+end_org """)


        fileToExportedZip = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        path_exportedZip = pathlib.Path(fileToExportedZip).expanduser().resolve(strict=True)
        print(myLinkedInBase)
        path_myLinkedInBase = pathlib.Path(myLinkedInBase).expanduser().resolve(strict=True)

        dateStr = extract_date_from_filename(path_exportedZip)

        dataExportDir = pathlib.Path(f"LinkedInDataExport_{dateStr}")
        path_dataExportDir = path_myLinkedInBase.joinpath(dataExportDir)

        if path_dataExportDir.is_dir():
            pass
            # return failed(cmndOutcome)
        else:
            utils.LinkedinBaseUtils.unzip_file(path_exportedZip, path_dataExportDir)

        dataExportSelected = path_myLinkedInBase.joinpath(pathlib.Path(f"LinkedInDataExport_selected"))

        refresh_symlink(dataExportSelected, path_dataExportDir)

        vcardsDir = pathlib.Path(f"LinkedInVCards_{dateStr}")
        path_vcardsDir = path_myLinkedInBase.joinpath(vcardsDir)

        print(dateStr)
        print(path_myLinkedInBase)
        print(path_dataExportDir)
        print(path_vcardsDir)

        return cmndOutcome.set(opResults=path_exportedZip,)



####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="pathToExportedZip",
            argDefault='',
            argChoices=[],
            argDescription="Path to the LinkedIn Basic_LinkedInDataExport_DATE.zip file."
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vcardsInvitations" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "myLinkedInBase vcardsDir" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vcardsInvitations>>  =verify= parsOpt=myLinkedInBase vcardsDir argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vcardsInvitations(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'myLinkedInBase', 'vcardsDir', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             myLinkedInBase: typing.Optional[str]=None,  # Cs Optional Param
             vcardsDir: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'myLinkedInBase': myLinkedInBase, 'vcardsDir': vcardsDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        myLinkedInBase = csParam.mappedValue('myLinkedInBase', myLinkedInBase)
        vcardsDir = csParam.mappedValue('vcardsDir', vcardsDir)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns runFacterAndGetJsonOutputBytes.
        #+end_org """)


        inFile = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        path_inFile = pathlib.Path(inFile).expanduser().resolve(strict=True)
        print(path_inFile)

        if vcardsDir is not None:
            path_vcardsDir = pathlib.Path(vcardsDir).expanduser().resolve(strict=True)

        print(path_vcardsDir)

        augmentation = invitations.LinkedInInvitations(path_inFile)

        augmentation.load()

        augmentation.augment_vcards(path_vcardsDir)

        return cmndOutcome.set(opResults=path_vcardsDir,)



####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="inFile",
            argDefault='',
            argChoices=[],
            argDescription="Path to the Exported LinkedIn connections file."
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vcardsMessages" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "myLinkedInBase vcardsDir" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vcardsMessages>>  =verify= parsOpt=myLinkedInBase vcardsDir argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vcardsMessages(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'myLinkedInBase', 'vcardsDir', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             myLinkedInBase: typing.Optional[str]=None,  # Cs Optional Param
             vcardsDir: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'myLinkedInBase': myLinkedInBase, 'vcardsDir': vcardsDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        myLinkedInBase = csParam.mappedValue('myLinkedInBase', myLinkedInBase)
        vcardsDir = csParam.mappedValue('vcardsDir', vcardsDir)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns runFacterAndGetJsonOutputBytes.
        #+end_org """)


        inFile = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        path_inFile = pathlib.Path(inFile).expanduser().resolve(strict=True)
        print(path_inFile)

        if vcardsDir is not None:
            path_vcardsDir = pathlib.Path(vcardsDir).expanduser().resolve(strict=True)

        print(path_vcardsDir)

        augmentation = messages.LinkedInMessages(path_inFile)

        augmentation.load()

        augmentation.augment_vcards(path_vcardsDir)

        return cmndOutcome.set(opResults=path_vcardsDir,)



####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="inFile",
            argDefault='',
            argChoices=[],
            argDescription="Path to the Exported LinkedIn connections file."
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "messages822" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "myLinkedInBase" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<messages822>>  =verify= parsOpt=myLinkedInBase argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class messages822(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'myLinkedInBase', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             myLinkedInBase: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'myLinkedInBase': myLinkedInBase, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        myLinkedInBase = csParam.mappedValue('myLinkedInBase', myLinkedInBase)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns runFacterAndGetJsonOutputBytes.
        #+end_org """)


        inFile = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        csv_path = pathlib.Path("~/linkedin/messages.csv")
        maildir_path = pathlib.Path("~/Maildir/LinkedIn")

        # telemetry = Telemetry("LinkedInMessages822")
        # converter = messages822.LinkedInMessagesToMaildir(csv_path, maildir_path, telemetry)
        converter = messages822.LinkedInMessagesToMaildir(csv_path, maildir_path)
        converter.run()


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="inFile",
            argDefault='',
            argChoices=[],
            argDescription="Path to the Exported LinkedIn connections file."
        )

        return cmndArgsSpecDict






####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
