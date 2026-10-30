# `SBFLockScreenDateView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 33 instance variables, 34 properties, 89 instance methods, 4 class methods

## Instance variables

```
@"SBUILegibilityLabel" _timeLabel;
d _timeAlpha;
d _subtitleAlpha;
@"SBFLockScreenDateSubtitleDateView" _dateSubtitleView;
@"<UITraitChangeRegistration>" _contentSizeCategoryTraitChangeRegistration;
@"SBFLockScreenDateSubtitleView" _customSubtitleView;
@"UIView" _activeSubtitleView;
@"NSTimeZone" _timeZone;
B _timeSupportsStretch;
B _hidesTime;
B _useLandscapeTimeFontSize;
B _useCompactDateFormat;
B _subtitleOnTop;
B _posterHasComplications;
B _restrictsVibrancy;
@"NSDate" _date;
@"UIColor" _overrideTextColor;
@"BSUIVibrancyConfiguration" _vibrancyConfiguration;
@"_UILegibilitySettings" _legibilitySettings;
d _alignmentPercent;
d _dateToTimeStretch;
d _maximumAdaptiveTimeTextHeight;
@"<PRPosterContentStyle>" _contentStyle;
d _timeLegibilityStrength;
d _subtitleLegibilityStrength;
d _maximumSubtitleWidth;
q _timeGlassInterfaceStyle;
@"UIFont" _customTimeFont;
@"NSString" _customTimeNumberingSystem;
@"UIView" _inlineComplicationView;
@"CSProminentDisplayViewController" _prominentDisplayViewController;
{?="ascender"d"descender"d"bodyLeading"d"capHeight"d} _customTimeMetrics;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _restingFrame;
```

## Properties

```
@property (TB,N,V_restrictsVibrancy) restrictsVibrancy;
@property (TB,N,GisSubtitleHidden) subtitleHidden;
@property (TB,N,V_useLandscapeTimeFontSize) useLandscapeTimeFontSize;
@property (TB,N,V_useCompactDateFormat) useCompactDateFormat;
@property (TB,D,N,GisPermanentCompactTimeEnabled) permanentCompactTimeEnabled;
@property (T@"NSDate",&,N,V_date) date;
@property (T@"UIColor",&,N,V_overrideTextColor) textColor;
@property (T@"<PRPosterContentStyle>",&,N,V_contentStyle) contentStyle;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
@property (Td,N,V_timeLegibilityStrength) timeLegibilityStrength;
@property (Td,N,V_subtitleLegibilityStrength) subtitleLegibilityStrength;
@property (Td,N,V_alignmentPercent) alignmentPercent;
@property (Td,N,V_dateToTimeStretch) dateToTimeStretch;
@property (Td,N,V_maximumSubtitleWidth) maximumSubtitleWidth;
@property (Td,N,V_maximumAdaptiveTimeTextHeight) maximumAdaptiveTimeTextHeight;
@property (Tq,N,V_timeGlassInterfaceStyle) timeGlassInterfaceStyle;
@property (T@"UIFont",C,N,V_customTimeFont) customTimeFont;
@property (T{?=dddd},R,N,V_customTimeMetrics) customTimeMetrics;
@property (TB,N,V_timeSupportsStretch) timeSupportsStretch;
@property (TB,N,V_subtitleOnTop) subtitleOnTop;
@property (T@"NSString",C,N,V_customTimeNumberingSystem) customTimeNumberingSystem;
@property (T@"BSUIVibrancyConfiguration",&,N,V_vibrancyConfiguration) vibrancyConfiguration;
@property (T@"UIView",R,N) timeView;
@property (TB,N,V_hidesTime) hidesTime;
@property (Td,R,N) timeBaselineOffsetFromOrigin;
@property (Td,R,N) subtitleBaselineOffsetFromOrigin;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_restingFrame) restingFrame;
@property (Td,R,N) timeAlpha;
@property (Td,R,N) subtitleAlpha;
@property (T@"SBFLockScreenDateSubtitleView",&,N,V_customSubtitleView) customSubtitleView;
@property (T@"UIView",&,N,V_inlineComplicationView) inlineComplicationView;
@property (TB,N,V_posterHasComplications) posterHasComplications;
@property (TB,D,N) wantsLeadingAlignedContent;
@property (T@"CSProminentDisplayViewController",&,N,V_prominentDisplayViewController) prominentDisplayViewController;
```

## Class methods

```
+[SBFLockScreenDateView defaultHeight];
+[SBFLockScreenDateView timeFont];
+[SBFLockScreenDateView metricsForFont:];
+[SBFLockScreenDateView timeFontMetrics];
```

## Instance methods

```
-[SBFLockScreenDateView setVibrancyConfiguration:];
-[SBFLockScreenDateView hidesTime];
-[SBFLockScreenDateView contentStyle];
-[SBFLockScreenDateView setCustomSubtitleView:];
-[SBFLockScreenDateView setContentStyle:];
-[SBFLockScreenDateView setWantsLeadingAlignedContent:];
-[SBFLockScreenDateView setHidesTime:];
-[SBFLockScreenDateView timeAlpha];
-[SBFLockScreenDateView isSubtitleHidden];
-[SBFLockScreenDateView _setDate:inTimeZone:];
-[SBFLockScreenDateView presentationExtentForAlignmentPercent:];
-[SBFLockScreenDateView timeView];
-[SBFLockScreenDateView timeGlassInterfaceStyle];
-[SBFLockScreenDateView prominentDisplayViewController];
-[SBFLockScreenDateView _timeLabel];
-[SBFLockScreenDateView vibrancyConfiguration];
-[SBFLockScreenDateView useCompactDateFormat];
-[SBFLockScreenDateView setDate:];
-[SBFLockScreenDateView textColor];
-[SBFLockScreenDateView setUseCompactDateFormat:];
-[SBFLockScreenDateView setMaximumSubtitleWidth:];
-[SBFLockScreenDateView customSubtitleView];
-[SBFLockScreenDateView updateFormat];
-[SBFLockScreenDateView customTimeNumberingSystem];
-[SBFLockScreenDateView maximumAdaptiveTimeTextHeight];
-[SBFLockScreenDateView wantsLeadingAlignedContent];
-[SBFLockScreenDateView setMaximumAdaptiveTimeTextHeight:];
-[SBFLockScreenDateView _updatePreferredContentSizeCategoryForEnvironment:previousTraitCollection:];
-[SBFLockScreenDateView dealloc];
-[SBFLockScreenDateView setTextColor:];
-[SBFLockScreenDateView setInlineComplicationView:];
-[SBFLockScreenDateView timeSupportsStretch];
-[SBFLockScreenDateView _timeLabelInsetsForTimeString:];
-[SBFLockScreenDateView isPermanentCompactTimeEnabled];
-[SBFLockScreenDateView subtitleOnTop];
-[SBFLockScreenDateView maximumSubtitleWidth];
-[SBFLockScreenDateView _subtitleViewFrameForView:alignmentPercent:];
-[SBFLockScreenDateView layoutSubviews];
-[SBFLockScreenDateView _timeLabelFrameForAlignmentPercent:];
-[SBFLockScreenDateView subtitleBaselineOffsetFromOrigin];
-[SBFLockScreenDateView setCustomTimeNumberingSystem:];
-[SBFLockScreenDateView restingFrame];
-[SBFLockScreenDateView customTimeMetrics];
-[SBFLockScreenDateView date];
-[SBFLockScreenDateView subtitleLegibilityStrength];
-[SBFLockScreenDateView setPosterHasComplications:];
-[SBFLockScreenDateView setPermanentCompactTimeEnabled:];
-[SBFLockScreenDateView sizeThatFits:];
-[SBFLockScreenDateView timeBaselineOffsetFromOrigin];
-[SBFLockScreenDateView setSubtitleOnTop:];
-[SBFLockScreenDateView _setSubtitleAlpha:];
-[SBFLockScreenDateView subtitleAlpha];
-[SBFLockScreenDateView _cacheCustomTimeMetrics];
-[SBFLockScreenDateView inlineComplicationView];
-[SBFLockScreenDateView customTimeFont];
-[SBFLockScreenDateView setRestrictsVibrancy:];
-[SBFLockScreenDateView chargingVisualInformationTimeSubtitleFrame];
-[SBFLockScreenDateView setSubtitleLegibilityStrength:];
-[SBFLockScreenDateView setTimeSupportsStretch:];
-[SBFLockScreenDateView setRestingFrame:];
-[SBFLockScreenDateView _updateLabels];
-[SBFLockScreenDateView setProminentDisplayViewController:];
-[SBFLockScreenDateView restrictsVibrancy];
-[SBFLockScreenDateView timeLegibilityStrength];
-[SBFLockScreenDateView setTimeGlassInterfaceStyle:];
-[SBFLockScreenDateView setUseLandscapeTimeFontSize:];
-[SBFLockScreenDateView dateToTimeStretch];
-[SBFLockScreenDateView _updateAdaptiveTime];
-[SBFLockScreenDateView legibilitySettings];
-[SBFLockScreenDateView setCustomTimeFont:];
-[SBFLockScreenDateView useLandscapeTimeFontSize];
-[SBFLockScreenDateView setAlignmentPercent:];
-[SBFLockScreenDateView _layoutSubtitle];
-[SBFLockScreenDateView _effectiveTextColor];
-[SBFLockScreenDateView setCompactFont:];
-[SBFLockScreenDateView _updateUsesCompactDateFormat];
-[SBFLockScreenDateView _updateLabelAlpha];
-[SBFLockScreenDateView setSubtitleHidden:];
-[SBFLockScreenDateView setLegibilitySettings:];
-[SBFLockScreenDateView _updateActiveSubtitleView];
-[SBFLockScreenDateView setTimeAlpha:subtitleAlpha:];
-[SBFLockScreenDateView _updateForNewFont];
-[SBFLockScreenDateView posterHasComplications];
-[SBFLockScreenDateView chargingVisualInformationTimeFrame];
-[SBFLockScreenDateView _cachedGlyphInsetsTimeFontForString:];
-[SBFLockScreenDateView initWithFrame:];
-[SBFLockScreenDateView alignmentPercent];
-[SBFLockScreenDateView setDateToTimeStretch:];
-[SBFLockScreenDateView setTimeLegibilityStrength:];
```
