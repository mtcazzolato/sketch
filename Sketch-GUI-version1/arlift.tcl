#############################################################################
# Generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#  Sep 13, 2021 12:09:09 PM -03  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Absolute
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1366x665+231+276
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Sketch - Association Rules with Lift Correlation"
    vTcl:DefineAlias "$top" "ToplevelARL" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    canvas $top.can45 \
        -background $vTcl(actual_gui_bg) -borderwidth 1 -closeenough 1.0 \
        -height 480 -highlightcolor black -insertbackground black \
        -relief ridge -selectbackground blue -selectforeground white \
        -width 680 
    vTcl:DefineAlias "$top.can45" "CanvasPlotAR" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr45 \
        -borderwidth 1 -relief groove -width 665 -height 480 
    vTcl:DefineAlias "$top.tFr45" "TFrameData" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa45 \
        -text {Attribute Selection} -width 520 -height 124 
    vTcl:DefineAlias "$top.tLa45" "TLabelframeDataSelection" vTcl:WidgetProc "ToplevelARL" 1
    set site_3_0 $top.tLa45
    ttk::label $site_3_0.tLa46 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Attribute: 
    vTcl:DefineAlias "$site_3_0.tLa46" "TLabelAttribute_1" vTcl:WidgetProc "ToplevelARL" 1
    ttk::combobox $site_3_0.tCo47 \
        -font TkTextFont -state readonly -foreground {} -background {} 
    vTcl:DefineAlias "$site_3_0.tCo47" "TComboboxSelectedAttribute" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu48 \
        -command btnAddAttToList -takefocus {} -text {Select Attribute} 
    vTcl:DefineAlias "$site_3_0.tBu48" "TButtonAddAttribute" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu50 \
        -command btnRemoveAttFromList -takefocus {} -text {Remove Attribute} 
    vTcl:DefineAlias "$site_3_0.tBu50" "TButtonRemoveAttribute" vTcl:WidgetProc "ToplevelARL" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_3_0.scr45 \
        -background $vTcl(actual_gui_bg) -height 107 -highlightcolor black \
        -width 176 
    vTcl:DefineAlias "$site_3_0.scr45" "ScrolledlistboxSelectedAttributes" vTcl:WidgetProc "ToplevelARL" 1

    $site_3_0.scr45.01 configure -background white \
        -cursor xterm \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightcolor #d9d9d9 \
        -selectbackground blue \
        -selectforeground white \
        -selectmode single \
        -width 10 \
        -listvariable listSelectedAttributesVar
    place $site_3_0.tLa46 \
        -in $site_3_0 -x 15 -y 19 -width 72 -relwidth 0 -height 17 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tCo47 \
        -in $site_3_0 -x 91 -y 16 -width 229 -relwidth 0 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu48 \
        -in $site_3_0 -x 14 -y 46 -width 305 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu50 \
        -in $site_3_0 -x 14 -y 84 -width 305 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr45 \
        -in $site_3_0 -x 332 -y 10 -width 176 -relwidth 0 -height 107 \
        -relheight 0 -anchor nw -bordermode ignore 
    vTcl:copy_lock $top.tLa45
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa46 \
        -text {Discover Association Rules} -width 730 -height 125 
    vTcl:DefineAlias "$top.tLa46" "TLabelframe1" vTcl:WidgetProc "ToplevelARL" 1
    set site_3_0 $top.tLa46
    ttk::label $site_3_0.tLa50 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {} -relief flat -anchor w -justify left -text {Min. Sup.:} 
    vTcl:DefineAlias "$site_3_0.tLa50" "TLabel1" vTcl:WidgetProc "ToplevelARL" 1
    ttk::label $site_3_0.tLa51 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {} -relief flat -anchor w -justify left -text {Min. Conf.:} 
    vTcl:DefineAlias "$site_3_0.tLa51" "TLabel2" vTcl:WidgetProc "ToplevelARL" 1
    spinbox $site_3_0.spi52 \
        -activebackground #f9f9f9 -background white -font TkDefaultFont \
        -foreground black -from 0.0 -highlightbackground black \
        -highlightcolor black -increment 0.05 -insertbackground black \
        -selectbackground blue -selectforeground white \
        -textvariable spinboxMinSupport -to 1.0 
    vTcl:DefineAlias "$site_3_0.spi52" "SpinboxMinSup" vTcl:WidgetProc "ToplevelARL" 1
    spinbox $site_3_0.spi53 \
        -activebackground #f9f9f9 -background white -font TkDefaultFont \
        -foreground black -from 0.0 -highlightbackground black \
        -highlightcolor black -increment 0.05 -insertbackground black \
        -selectbackground blue -selectforeground white \
        -textvariable spinboxMinConfidence -to 1.0 
    vTcl:DefineAlias "$site_3_0.spi53" "SpinboxMinConf" vTcl:WidgetProc "ToplevelARL" 1
    ttk::separator $site_3_0.tSe54 \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe54" "TSeparator1" vTcl:WidgetProc "ToplevelARL" 1
    entry $site_3_0.ent55 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable entryInputTransactionsVar \
        -width 216 
    vTcl:DefineAlias "$site_3_0.ent55" "EntryInputTransactions" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu56 \
        -command btnLoadTransactions -takefocus {} -text ... 
    vTcl:DefineAlias "$site_3_0.tBu56" "TButtonLoadTransactions" vTcl:WidgetProc "ToplevelARL" 1
    ttk::label $site_3_0.tLa57 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {} -relief flat -anchor w -justify left -text Transactions: 
    vTcl:DefineAlias "$site_3_0.tLa57" "TLabel1_1" vTcl:WidgetProc "ToplevelARL" 1
    ttk::label $site_3_0.tLa58 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {} -relief flat -anchor w -justify left -text {A. Rules:} 
    vTcl:DefineAlias "$site_3_0.tLa58" "TLabel1_1_1" vTcl:WidgetProc "ToplevelARL" 1
    entry $site_3_0.ent59 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable entryInputRulesVar -width 216 
    vTcl:DefineAlias "$site_3_0.ent59" "EntryInputAssociationRules" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu60 \
        -command btnLoadARules -takefocus {} -text ... 
    vTcl:DefineAlias "$site_3_0.tBu60" "TButtonLoadARules" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu62 \
        -command btnVisualizeSankeyDiagram -takefocus {} \
        -text {Static Sankey Diagram} 
    vTcl:DefineAlias "$site_3_0.tBu62" "TButtonVisualizeSankeyDiagram" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu45 \
        -command btnDiscoverARL -takefocus {} -text {Discover A. Rules} 
    vTcl:DefineAlias "$site_3_0.tBu45" "TButtonDiscoverARL" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu46 \
        -command btnLoadFilesAR -takefocus {} \
        -text {Load Files with Transactions and A. Rules} 
    vTcl:DefineAlias "$site_3_0.tBu46" "TButtonLoadFilesAR" vTcl:WidgetProc "ToplevelARL" 1
    ttk::separator $site_3_0.tSe48 \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe48" "TSeparator1_1" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu53 \
        -command btnVisualizeSankeyDiagramHTML -takefocus {} \
        -text {Dinamic Sankey Diagram} 
    vTcl:DefineAlias "$site_3_0.tBu53" "TButtonVisualizeSankeyDiagramHTML" vTcl:WidgetProc "ToplevelARL" 1
    ttk::label $site_3_0.tLa54 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {} -relief flat -anchor w -justify left \
        -text {AR Visualization} -compound center 
    vTcl:DefineAlias "$site_3_0.tLa54" "TLabel1_1_2" vTcl:WidgetProc "ToplevelARL" 1
    place $site_3_0.tLa50 \
        -in $site_3_0 -x 10 -y 20 -width 97 -relwidth 0 -height 14 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa51 \
        -in $site_3_0 -x 10 -y 44 -width 97 -relwidth 0 -height 14 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.spi52 \
        -in $site_3_0 -x 98 -y 18 -width 57 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.spi53 \
        -in $site_3_0 -x 98 -y 42 -width 57 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSe54 \
        -in $site_3_0 -x 174 -y 15 -relwidth 0 -height 100 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $site_3_0.ent55 \
        -in $site_3_0 -x 294 -y 14 -width 216 -relwidth 0 -height 26 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu56 \
        -in $site_3_0 -x 511 -y 15 -width 25 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa57 \
        -in $site_3_0 -x 184 -y 22 -width 97 -relwidth 0 -height 14 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa58 \
        -in $site_3_0 -x 185 -y 47 -width 87 -relwidth 0 -height 14 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent59 \
        -in $site_3_0 -x 294 -y 40 -width 216 -relwidth 0 -height 26 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu60 \
        -in $site_3_0 -x 511 -y 42 -width 25 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu62 \
        -in $site_3_0 -x 548 -y 43 -width 175 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu45 \
        -in $site_3_0 -x 10 -y 70 -width 145 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu46 \
        -in $site_3_0 -x 182 -y 70 -width 355 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSe48 \
        -in $site_3_0 -x 543 -y 13 -width 1 -relwidth 0 -height 100 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu53 \
        -in $site_3_0 -x 548 -y 79 -width 175 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa54 \
        -in $site_3_0 -x 551 -y 20 -width 167 -relwidth 0 -height 14 \
        -relheight 0 -anchor nw -bordermode ignore 
    vTcl:copy_lock $top.tLa46
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu49 \
        -command btnCloseARL -takefocus {} -text Close 
    vTcl:DefineAlias "$top.tBu49" "TButtonCloseARL" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu50 \
        -command btnSaveSankeyImage -takefocus {} -text {Save Sankey Image} 
    vTcl:DefineAlias "$top.tBu50" "TButtonSaveSankeyImage" vTcl:WidgetProc "ToplevelARL" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu51 \
        -command btnSaveRulesTransactions -takefocus {} \
        -text {Save Discovered Rules and Transactions} 
    vTcl:DefineAlias "$top.tBu51" "TButtonSaveRulesTransactions" vTcl:WidgetProc "ToplevelARL" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can45 \
        -in $top -x 678 -y 136 -width 680 -relwidth 0 -height 482 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.tFr45 \
        -in $top -x 10 -y 137 -width 665 -relwidth 0 -height 480 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa45 \
        -in $top -x 10 -y 2 -width 520 -relwidth 0 -height 124 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa46 \
        -in $top -x 537 -y 2 -width 730 -relwidth 0 -height 125 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu49 \
        -in $top -x 1272 -y 8 -width 85 -relwidth 0 -height 118 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu50 \
        -in $top -x 680 -y 623 -width 675 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu51 \
        -in $top -x 10 -y 623 -width 665 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

