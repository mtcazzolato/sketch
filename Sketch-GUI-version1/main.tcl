#############################################################################
# Generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#  Sep 10, 2021 12:07:23 PM -03  platform: Linux
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
    wm geometry $top 1401x755+995+149
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "Sketch - Similarity Search Supported by Correlation Methods - Data Overview"
    vTcl:DefineAlias "$top" "ToplevelCompTuple" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr45 \
        -borderwidth 1 -relief groove -width 1380 -height 406 
    vTcl:DefineAlias "$top.tFr45" "TFrameDataMainPage" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa58 \
        -text {Input Data} -width 628 -height 86 
    vTcl:DefineAlias "$top.tLa58" "TLabelframe1" vTcl:WidgetProc "ToplevelCompTuple" 1
    set site_3_0 $top.tLa58
    ttk::label $site_3_0.tLa59 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {Input data file} 
    vTcl:DefineAlias "$site_3_0.tLa59" "TLabelInputData" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::label $site_3_0.tLa60 \
        -background #f4f4f4 -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -borderwidth 2 -relief flat -anchor w \
        -justify left -textvariable VarInputFile 
    vTcl:DefineAlias "$site_3_0.tLa60" "TLabelInputFileDisplay" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu61 \
        -command btnSelectFile -takefocus {} -text {Choose File} 
    vTcl:DefineAlias "$site_3_0.tBu61" "btnSelectFile" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu62 \
        -command btnLoadFile -takefocus {} -text {Load Data} 
    vTcl:DefineAlias "$site_3_0.tBu62" "btnLoadFile" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::label $site_3_0.tLa45 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {} -relief flat -anchor w -justify left \
        -text {Input data types file} 
    vTcl:DefineAlias "$site_3_0.tLa45" "TLabelInputDataTypes" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::label $site_3_0.tLa47 \
        -background #f4f4f4 -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -borderwidth 2 -relief flat -anchor w \
        -justify left -textvariable VarInputFileDataType 
    vTcl:DefineAlias "$site_3_0.tLa47" "TLabelInputFileDisplay_1" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu50 \
        -command btnSelectFileDataType -takefocus {} -text {Choose File} 
    vTcl:DefineAlias "$site_3_0.tBu50" "btnSelectFileDataType" vTcl:WidgetProc "ToplevelCompTuple" 1
    place $site_3_0.tLa59 \
        -in $site_3_0 -x 20 -y 19 -width 124 -relwidth 0 -height 26 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa60 \
        -in $site_3_0 -x 130 -y 13 -width 284 -relwidth 0 -height 27 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu61 \
        -in $site_3_0 -x 419 -y 11 -width 96 -relwidth 0 -height 32 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu62 \
        -in $site_3_0 -x 523 -y 12 -width 94 -relwidth 0 -height 66 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa45 \
        -in $site_3_0 -x 20 -y 49 -width 107 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa47 \
        -in $site_3_0 -x 130 -y 47 -width 284 -relwidth 0 -height 27 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu50 \
        -in $site_3_0 -x 419 -y 46 -width 96 -relwidth 0 -height 32 \
        -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa45 \
        -text {Connect Database} -width 738 -height 86 
    vTcl:DefineAlias "$top.tLa45" "TLabelframeDatabaseConnection" vTcl:WidgetProc "ToplevelCompTuple" 1
    set site_3_0 $top.tLa45
    ttk::label $site_3_0.tLa59 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {DB Name:} 
    vTcl:DefineAlias "$site_3_0.tLa59" "TLabelDBName" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu62 \
        -command btnLoadDatabase -takefocus {} -text {Load Database} 
    vTcl:DefineAlias "$site_3_0.tBu62" "btnLoadDBConfigFile" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::label $site_3_0.tLa46 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {} -relief flat -anchor w -justify left -text Username: 
    vTcl:DefineAlias "$site_3_0.tLa46" "TLabelInputUsername" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::entry $site_3_0.tEn48 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn48" "TEntryDBName" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::entry $site_3_0.tEn49 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn49" "TEntryUsername" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::entry $site_3_0.tEn50 \
        -font TkTextFont -show * -foreground {} -background {} -takefocus {} \
        -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn50" "TEntryPassword" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::label $site_3_0.tLa51 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text Password: 
    vTcl:DefineAlias "$site_3_0.tLa51" "TLabelPassword" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu52 \
        -command btnSaveDatabaseConfigFile -takefocus {} \
        -text {Save Database Configuration File} 
    vTcl:DefineAlias "$site_3_0.tBu52" "TButtonSaveDatabaseConfigFile" vTcl:WidgetProc "ToplevelCompTuple" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_3_0.scr53 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_3_0.scr53" "ScrolledlistboxDBTables" vTcl:WidgetProc "ToplevelCompTuple" 1

    $site_3_0.scr53.01 configure -background white \
        -cursor xterm \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightcolor #d9d9d9 \
        -selectbackground blue \
        -selectforeground white \
        -width 10 \
        -listvariable listDBTablesVar
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu54 \
        -command btnLoadSelectedTable -takefocus {} -text {Load Table} 
    vTcl:DefineAlias "$site_3_0.tBu54" "btnLoadSelectedTable" vTcl:WidgetProc "ToplevelCompTuple" 1
    ttk::separator $site_3_0.tSe55 \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe55" "TSeparator1" vTcl:WidgetProc "ToplevelCompTuple" 1
    place $site_3_0.tLa59 \
        -in $site_3_0 -x 10 -y 20 -width 64 -relwidth 0 -height 16 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu62 \
        -in $site_3_0 -x 11 -y 45 -width 204 -relwidth 0 -height 35 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa46 \
        -in $site_3_0 -x 153 -y 20 -width 71 -relwidth 0 -height 14 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn48 \
        -in $site_3_0 -x 67 -y 14 -width 80 -relwidth 0 -height 26 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn49 \
        -in $site_3_0 -x 218 -y 14 -width 90 -relwidth 0 -height 26 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn50 \
        -in $site_3_0 -x 379 -y 14 -width 80 -relwidth 0 -height 26 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa51 \
        -in $site_3_0 -x 312 -y 19 -width 64 -relwidth 0 -height 16 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu52 \
        -in $site_3_0 -x 221 -y 45 -width 244 -relwidth 0 -height 35 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr53 \
        -in $site_3_0 -x 485 -y 12 -width 146 -relwidth 0 -height 67 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu54 \
        -in $site_3_0 -x 636 -y 12 -width 94 -relwidth 0 -height 67 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tSe55 \
        -in $site_3_0 -x 476 -y 15 -relwidth 0 -height 60 -relheight 0 \
        -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa49 \
        -text {Database Query} -width 1380 -height 145 
    vTcl:DefineAlias "$top.tLa49" "TLabelframeQuery" vTcl:WidgetProc "ToplevelCompTuple" 1
    set site_3_0 $top.tLa49
    button $site_3_0.but51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command btnRunQuery \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text {Run Query} 
    vTcl:DefineAlias "$site_3_0.but51" "btnRunQuery" vTcl:WidgetProc "ToplevelCompTuple" 1
    button $site_3_0.but52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command btnClearQueryField \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text Clear 
    vTcl:DefineAlias "$site_3_0.but52" "btnClear" vTcl:WidgetProc "ToplevelCompTuple" 1
    entry $site_3_0.ent53 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable VarQueryText -width 1206 
    vTcl:DefineAlias "$site_3_0.ent53" "EntryQuery" vTcl:WidgetProc "ToplevelCompTuple" 1
    place $site_3_0.but51 \
        -in $site_3_0 -x 1220 -y 82 -width 150 -relwidth 0 -height 55 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but52 \
        -in $site_3_0 -x 1220 -y 20 -width 150 -relwidth 0 -height 55 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent53 \
        -in $site_3_0 -x 10 -y 20 -width 1206 -relwidth 0 -height 117 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab46 \
        -font TkDefaultFont -foreground black -text {Analysis tasks} \
        -background $vTcl(actual_gui_bg) -height 65 -highlightcolor black \
        -width 990 
    vTcl:DefineAlias "$top.lab46" "LabelframeSketchTakss" vTcl:WidgetProc "ToplevelCompTuple" 1
    set site_3_0 $top.lab46
    button $site_3_0.but47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command btnOpenSimWindow \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text {Similarity Search} 
    vTcl:DefineAlias "$site_3_0.but47" "btnOpenSimWindow" vTcl:WidgetProc "ToplevelCompTuple" 1
    button $site_3_0.but50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command btnOpenARLiftWindow \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text {Association Rules with Lift Correlation} 
    vTcl:DefineAlias "$site_3_0.but50" "btnOpenARLiftWindow" vTcl:WidgetProc "ToplevelCompTuple" 1
    button $site_3_0.but45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command btnOpenAnovaWindow \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text {Analysis of Variance (ANOVA)} 
    vTcl:DefineAlias "$site_3_0.but45" "ButtonOpenAnovaWindow" vTcl:WidgetProc "ToplevelCompTuple" 1
    place $site_3_0.but47 \
        -in $site_3_0 -x 10 -y 21 -width 320 -relwidth 0 -height 35 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but50 \
        -in $site_3_0 -x 337 -y 21 -width 320 -relwidth 0 -height 35 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 660 -y 21 -width 320 -relwidth 0 -height 35 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command btnExit -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text {Exit >} 
    vTcl:DefineAlias "$top.but49" "btnExit" vTcl:WidgetProc "ToplevelCompTuple" 1
    button $top.but47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command btnAbout \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text {About Sketch} 
    vTcl:DefineAlias "$top.but47" "ButtonAbout" vTcl:WidgetProc "ToplevelCompTuple" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tFr45 \
        -in $top -x 10 -y 270 -width 1380 -relwidth 0 -height 406 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.tLa58 \
        -in $top -x 10 -y 10 -width 628 -relwidth 0 -height 86 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa45 \
        -in $top -x 651 -y 10 -width 738 -relwidth 0 -height 86 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa49 \
        -in $top -x 10 -y 108 -width 1380 -relwidth 0 -height 145 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 10 -y 680 -width 990 -relwidth 0 -height 65 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 1205 -y 685 -width 185 -relwidth 0 -height 58 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 1006 -y 686 -width 195 -relwidth 0 -height 58 \
        -relheight 0 -anchor nw -bordermode ignore 
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
