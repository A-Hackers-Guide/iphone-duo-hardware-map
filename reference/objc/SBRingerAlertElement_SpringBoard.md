# `SBRingerAlertElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertProvidedContentElement`
- Protocols: `SBSystemApertureContextProviding`, `SBRingerNoticeUICoordinating`
- 21 instance variables, 33 properties, 71 instance methods, 0 class methods

## Instance variables

```
B _ringerSilent;
B _activatedForPreviewing;
B _lastEventIsAVolumeChange;
f _volume;
@"<SAAlertHosting>" _alertHost;
Q _source;
@"<SBRingerAlertElementDelegate>" _delegate;
@"<SAInvalidatable>" _assertion;
Q _visualStyle;
@"SBUISystemApertureContentProvider" _contentProvider;
@"SBUISystemApertureCAPackageContentProvider" _leadingRingerContentViewProvider;
@"SBUISystemApertureCAPackageContentProvider" _minimalRingerContentViewProvider;
@"<SBUISystemApertureContentViewProviding>" _minimalContentViewProvider;
@"SBUISystemApertureTextContentProvider" _trailingTextContentViewProvider;
@"SBRingerVolumeSliderView" _sliderView;
@"SBRingerVolumeSliderView" _minimalSliderView;
@"UIImageView" _volumeBellImageView;
@"UILabel" _volumeLabel;
@"NSArray" _defaultVolumeConstraints;
@"NSArray" _limitedSizeVolumeConstraints;
d _overshoot;
```

## Properties

```
@property (TQ,N,V_visualStyle) visualStyle;
@property (T@"SBUISystemApertureContentProvider",&,N,V_contentProvider) contentProvider;
@property (T@"SBUISystemApertureCAPackageContentProvider",&,N,V_leadingRingerContentViewProvider) leadingRingerContentViewProvider;
@property (T@"SBUISystemApertureCAPackageContentProvider",&,N,V_minimalRingerContentViewProvider) minimalRingerContentViewProvider;
@property (T@"<SBUISystemApertureContentViewProviding>",&,N,V_minimalContentViewProvider) minimalContentViewProvider;
@property (T@"SBUISystemApertureTextContentProvider",&,N,V_trailingTextContentViewProvider) trailingTextContentViewProvider;
@property (T@"SBRingerVolumeSliderView",&,N,V_sliderView) sliderView;
@property (T@"SBRingerVolumeSliderView",&,N,V_minimalSliderView) minimalSliderView;
@property (T@"UIImageView",&,N,V_volumeBellImageView) volumeBellImageView;
@property (T@"UILabel",&,N,V_volumeLabel) volumeLabel;
@property (T@"NSArray",&,N,V_defaultVolumeConstraints) defaultVolumeConstraints;
@property (T@"NSArray",&,N,V_limitedSizeVolumeConstraints) limitedSizeVolumeConstraints;
@property (TB,N,V_lastEventIsAVolumeChange) lastEventIsAVolumeChange;
@property (Td,N,V_overshoot) overshoot;
@property (TQ,N,V_source) source;
@property (T@"<SBRingerAlertElementDelegate>",W,N,V_delegate) delegate;
@property (T@"<SAInvalidatable>",&,N,V_assertion) assertion;
@property (TB,N,GisActivatedForPreviewing,V_activatedForPreviewing) activatedForPreviewing;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisRingerSilent,V_ringerSilent) ringerSilent;
@property (Tf,N,V_volume) volume;
@property (TB,R,N,GisPresented) presented;
```

## Instance methods

```
-[SBRingerAlertElement setDisplayedWithLimitedSize:];
-[SBRingerAlertElement keyColor];
-[SBRingerAlertElement overridesConcentricPaddingForView:inLayoutMode:];
-[SBRingerAlertElement concentricPaddingOverrideForView:inLayoutMode:];
-[SBRingerAlertElement isPresented];
-[SBRingerAlertElement setAssertion:];
-[SBRingerAlertElement clientIdentifier];
-[SBRingerAlertElement isProvidedViewConcentric:inLayoutMode:];
-[SBRingerAlertElement setVisualStyle:];
-[SBRingerAlertElement assertion];
-[SBRingerAlertElement preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBRingerAlertElement elementIdentifier];
-[SBRingerAlertElement volume];
-[SBRingerAlertElement sliderView];
-[SBRingerAlertElement visualStyle];
-[SBRingerAlertElement setVolume:];
-[SBRingerAlertElement setContentProvider:];
-[SBRingerAlertElement setAlertHost:];
-[SBRingerAlertElement setSource:];
-[SBRingerAlertElement setDelegate:];
-[SBRingerAlertElement delegate];
-[SBRingerAlertElement contentProvider];
-[SBRingerAlertElement setSliderView:];
-[SBRingerAlertElement source];
-[SBRingerAlertElement alertHost];
-[SBRingerAlertElement minimalContentViewProvider];
-[SBRingerAlertElement setMinimalContentViewProvider:];
-[SBRingerAlertElement _updateStateWithTransitionType:];
-[SBRingerAlertElement setVolume:animated:forKeyPress:];
-[SBRingerAlertElement setVolumeLabel:];
-[SBRingerAlertElement trailingTextContentViewProvider];
-[SBRingerAlertElement _accessibilityLabelForRingerSilent:];
-[SBRingerAlertElement _applyVolumeLimitedSizeLayout:];
-[SBRingerAlertElement _bellImageForRingerSilent:];
-[SBRingerAlertElement _buildVolumeLeadingContentProviderForRingerSilent:];
-[SBRingerAlertElement _buildVolumeTrailingContentProvider];
-[SBRingerAlertElement _colorForRingerSilent:];
-[SBRingerAlertElement _containedVolumeSliderViewWithSize:layoutAxis:];
-[SBRingerAlertElement _getRingerPackageSizesForVisualStyle:ringerSilent:leadingSize:minimalSize:];
-[SBRingerAlertElement _minimalContentForSource:visualStyle:ringerSilent:];
-[SBRingerAlertElement _ringerPackageNameForVisualStyle:minimal:];
-[SBRingerAlertElement _setRingerSilent:skipUpdate:];
-[SBRingerAlertElement _shakeRingerBell];
-[SBRingerAlertElement _textForRingerSilent:];
-[SBRingerAlertElement _updateVolumeSliderAnimated:];
-[SBRingerAlertElement buttonReleased];
-[SBRingerAlertElement defaultVolumeConstraints];
-[SBRingerAlertElement initWithSource:ringerSilent:forPreviewing:];
-[SBRingerAlertElement isActivatedForPreviewing];
-[SBRingerAlertElement isRingerSilent];
-[SBRingerAlertElement lastEventIsAVolumeChange];
-[SBRingerAlertElement leadingRingerContentViewProvider];
-[SBRingerAlertElement limitedSizeVolumeConstraints];
-[SBRingerAlertElement minimalRingerContentViewProvider];
-[SBRingerAlertElement minimalSliderView];
-[SBRingerAlertElement nudgeUp:];
-[SBRingerAlertElement overshoot];
-[SBRingerAlertElement presentForMuteChange:];
-[SBRingerAlertElement setActivatedForPreviewing:];
-[SBRingerAlertElement setDefaultVolumeConstraints:];
-[SBRingerAlertElement setLastEventIsAVolumeChange:];
-[SBRingerAlertElement setLeadingRingerContentViewProvider:];
-[SBRingerAlertElement setLimitedSizeVolumeConstraints:];
-[SBRingerAlertElement setMinimalRingerContentViewProvider:];
-[SBRingerAlertElement setMinimalSliderView:];
-[SBRingerAlertElement setOvershoot:];
-[SBRingerAlertElement setRingerSilent:];
-[SBRingerAlertElement setTrailingTextContentViewProvider:];
-[SBRingerAlertElement setVolumeBellImageView:];
-[SBRingerAlertElement volumeBellImageView];
-[SBRingerAlertElement volumeLabel];
```
