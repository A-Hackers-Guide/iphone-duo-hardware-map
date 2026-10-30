# `UISliderDataModel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 27 instance variables, 26 properties, 64 instance methods, 0 class methods

## Instance variables

```
^{__CFDictionary=} _contentLookup;
@"_UIEdgeFeedbackGenerator" _edgeFeedbackGenerator;
@"_UIModulationFeedbackGenerator" _modulationFeedbackGenerator;
B _overrideMinimumEnabledValue;
B _overrideMaximumEnabledValue;
B _continuous;
B _showValue;
B _thumbEnabled;
B _trackEnabled;
B _minimumTrackVisible;
B _fluidTrackHidden;
B _userInteractionEnabled;
B _enabled;
B _highlighted;
B _selected;
B _tracking;
f _value;
f _minValue;
f _maxValue;
f _minEnabledValue;
f _maxEnabledValue;
f _sliderSpeedMultiplier;
@"UIImage" _minimumValueImage;
@"UIImage" _maximumValueImage;
@"UIColor" _minTintColor;
@"UIColor" _maxTintColor;
@"UIColor" _thumbTintColor;
```

## Properties

```
@property (Tf,R,N,V_value) value;
@property (Tf,R,N,V_minValue) minimumValue;
@property (Tf,R,N,V_maxValue) maximumValue;
@property (T@"UIImage",&,N,V_minimumValueImage) minimumValueImage;
@property (T@"UIImage",&,N,V_maximumValueImage) maximumValueImage;
@property (TB,N,GisContinuous,V_continuous) continuous;
@property (T@"UIColor",&,N,V_minTintColor) minimumTrackTintColor;
@property (T@"UIColor",&,N,V_maxTintColor) maximumTrackTintColor;
@property (T@"UIColor",&,N,V_thumbTintColor) thumbTintColor;
@property (TB,R,N) hasAnyThumbImage;
@property (TB,R,N) hasAnyTrackImage;
@property (Tf,R,N,V_minEnabledValue) minimumEnabledValue;
@property (Tf,R,N,V_maxEnabledValue) maximumEnabledValue;
@property (TB,N,V_showValue) showValue;
@property (TB,N,GisThumbEnabled,V_thumbEnabled) thumbEnabled;
@property (TB,N,GisTrackEnabled,V_trackEnabled) trackEnabled;
@property (TB,N,GisMinimumTrackVisible,V_minimumTrackVisible) minimumTrackVisible;
@property (TB,N,GisFluidTrackHidden,V_fluidTrackHidden) fluidTrackHidden;
@property (Tf,N,V_sliderSpeedMultiplier) sliderSpeedMultiplier;
@property (T@"_UIEdgeFeedbackGenerator",&,N) edgeFeedbackGenerator;
@property (T@"_UIModulationFeedbackGenerator",&,N) modulationFeedbackGenerator;
@property (TB,N,GisUserInteractionEnabled,V_userInteractionEnabled) userInteractionEnabled;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N,GisHighlighted,V_highlighted) highlighted;
@property (TB,N,GisSelected,V_selected) selected;
@property (TB,N,GisTracking,V_tracking) tracking;
```

## Instance methods

```
-[UISliderDataModel setUserInteractionEnabled:];
-[UISliderDataModel setMinimumTrackVisible:];
-[UISliderDataModel setSelected:];
-[UISliderDataModel setMaximumValue:];
-[UISliderDataModel setEdgeFeedbackGenerator:];
-[UISliderDataModel isUserInteractionEnabled];
-[UISliderDataModel hasAnyTrackImage];
-[UISliderDataModel minimumTrackTintColor];
-[UISliderDataModel maximumEnabledValue];
-[UISliderDataModel setTracking:];
-[UISliderDataModel setMaximumTrackImage:forState:];
-[UISliderDataModel setThumbImage:forState:];
-[UISliderDataModel init];
-[UISliderDataModel setModulationFeedbackGenerator:];
-[UISliderDataModel isMinimumTrackVisible];
-[UISliderDataModel isHighlighted];
-[UISliderDataModel setContinuous:];
-[UISliderDataModel dealloc];
-[UISliderDataModel value];
-[UISliderDataModel setMinimumValueImage:];
-[UISliderDataModel maximumTrackImageForState:];
-[UISliderDataModel sliderSpeedMultiplier];
-[UISliderDataModel maximumValueImage];
-[UISliderDataModel setMaximumValueImage:];
-[UISliderDataModel isContinuous];
-[UISliderDataModel isThumbEnabled];
-[UISliderDataModel isEnabled];
-[UISliderDataModel thumbImageForState:];
-[UISliderDataModel isTracking];
-[UISliderDataModel setSliderSpeedMultiplier:];
-[UISliderDataModel thumbTintColor];
-[UISliderDataModel minimumEnabledValue];
-[UISliderDataModel setMaximumTrackImage:forStates:];
-[UISliderDataModel setValue:];
-[UISliderDataModel setHighlighted:];
-[UISliderDataModel setMinimumValue:];
-[UISliderDataModel setShowValue:];
-[UISliderDataModel modulationFeedbackGenerator];
-[UISliderDataModel _setContent:forState:];
-[UISliderDataModel setEnabled:];
-[UISliderDataModel minimumValueImage];
-[UISliderDataModel hasAnyThumbImage];
-[UISliderDataModel minimumTrackImageForState:];
-[UISliderDataModel isSelected];
-[UISliderDataModel setFluidTrackHidden:];
-[UISliderDataModel setTrackEnabled:];
-[UISliderDataModel setMinimumTrackTintColor:];
-[UISliderDataModel setThumbImage:forStates:];
-[UISliderDataModel isFluidTrackHidden];
-[UISliderDataModel minimumValue];
-[UISliderDataModel setThumbTintColor:];
-[UISliderDataModel maximumTrackTintColor];
-[UISliderDataModel setMinimumEnabledValue:];
-[UISliderDataModel edgeFeedbackGenerator];
-[UISliderDataModel showValue];
-[UISliderDataModel setMinimumTrackImage:forState:];
-[UISliderDataModel setMinimumTrackImage:forStates:];
-[UISliderDataModel maximumValue];
-[UISliderDataModel _contentForState:];
-[UISliderDataModel setMaximumEnabledValue:];
-[UISliderDataModel isTrackEnabled];
-[UISliderDataModel _setValue:minValue:maxValue:minEnabledUsed:minEnabledValue:maxEnabledUsed:maxEnabledValue:];
-[UISliderDataModel setMaximumTrackTintColor:];
-[UISliderDataModel setThumbEnabled:];
```
