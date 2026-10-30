# `UICoverSheetButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `_UIClickInteractionDelegate_ForSpringBoardOnly`
- 20 instance variables, 15 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"UIView" _containerView;
@"UIImageView" _contentView;
@"UIVisualEffectView" _backgroundEffectView;
@"NSArray" _backgroundEffects;
@"NSArray" _selectedBackgroundEffects;
@"_UIClickInteraction" _clickInteraction;
B _interactive;
B _didActivateDuringInteraction;
d _maxForceDuringInteraction;
d _highlightProgress;
B _pronounced;
B _latching;
B _shouldUseContinuousCorners;
@"UIImage" _image;
@"UIImage" _selectedImage;
@"UIColor" _selectedTintColor;
@"NSString" _localizedAccessoryTitle;
@"NSString" _backgroundEffectViewGroupName;
@"NSString" _statisticsIdentifier;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _edgeInsets;
```

## Properties

```
@property (TB,N,GisPronounced,V_pronounced) pronounced;
@property (TB,N,GisLatching,V_latching) latching;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"UIImage",&,N,V_selectedImage) selectedImage;
@property (T@"UIColor",&,N,V_selectedTintColor) selectedTintColor;
@property (T{UIEdgeInsets=dddd},N,V_edgeInsets) edgeInsets;
@property (Tq,N) imageContentMode;
@property (TB,N,V_shouldUseContinuousCorners) shouldUseContinuousCorners;
@property (T@"NSString",C,N,V_localizedAccessoryTitle) localizedAccessoryTitle;
@property (T@"NSString",C,N,V_backgroundEffectViewGroupName) backgroundEffectViewGroupName;
@property (T@"NSString",C,N,V_statisticsIdentifier) statisticsIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UICoverSheetButton imageContentMode];
-[UICoverSheetButton setImageContentMode:];
-[UICoverSheetButton layoutIfNeededAnimated];
-[UICoverSheetButton setSelected:];
-[UICoverSheetButton _clickInteractionDefaultDriverType:];
-[UICoverSheetButton statisticsIdentifier];
-[UICoverSheetButton setStatisticsIdentifier:];
-[UICoverSheetButton setEdgeInsets:];
-[UICoverSheetButton layoutSubviews];
-[UICoverSheetButton _animateEffectUpdateWithProgress:ended:];
-[UICoverSheetButton clickInteractionDidEnd:];
-[UICoverSheetButton clickInteractionDidClickUp:];
-[UICoverSheetButton sizeThatFits:];
-[UICoverSheetButton clickInteraction:didObserveForce:];
-[UICoverSheetButton setBackgroundEffectViewGroupName:];
-[UICoverSheetButton selectedImage];
-[UICoverSheetButton highlightEffectForClickInteraction:];
-[UICoverSheetButton edgeInsets];
-[UICoverSheetButton setSelectedImage:];
-[UICoverSheetButton backgroundEffectViewGroupName];
-[UICoverSheetButton image];
-[UICoverSheetButton _backgroundEffectsWithBrightness:];
-[UICoverSheetButton initWithFrame:];
-[UICoverSheetButton clickInteractionShouldBegin:];
-[UICoverSheetButton setImage:];
-[UICoverSheetButton _firstActivationDurationStat];
-[UICoverSheetButton _interactionCountStatWithActivation:];
-[UICoverSheetButton _interactionDurationStat];
-[UICoverSheetButton _maxForceStatWithActivation:];
-[UICoverSheetButton isLatching];
-[UICoverSheetButton isPronounced];
-[UICoverSheetButton localizedAccessoryTitle];
-[UICoverSheetButton selectedTintColor];
-[UICoverSheetButton setLatching:];
-[UICoverSheetButton setLocalizedAccessoryTitle:];
-[UICoverSheetButton setPronounced:];
-[UICoverSheetButton setSelectedTintColor:];
-[UICoverSheetButton setShouldUseContinuousCorners:];
-[UICoverSheetButton shouldUseContinuousCorners];
```
