# `JFXOverlayEffect`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXTextEffect`
- Protocols: `JFXTrackedEffectPropertiesDelegate`
- 6 instance variables, 16 properties, 94 instance methods, 3 class methods

## Instance variables

```
Ai _isInteractiveEditingCount;
Ai _isEditingFaceTrackingTransformsCount;
B _prefersTrackingNotActivateAutomatically;
@"NSString" _accessibilityOverlayEffectLabel;
@"JFXTrackedEffectProperties" _trackingProps;
@"JFXFaceTrackedEffectTransform" _internalFaceTrackingTransform;
```

## Properties

```
@property (T@"JFXFaceTrackedEffectTransform",&,V_internalFaceTrackingTransform) internalFaceTrackingTransform;
@property (TB,D,N,GisHidden) hidden;
@property (T@"NSString",C,N,V_accessibilityOverlayEffectLabel) accessibilityOverlayEffectLabel;
@property (T@"JFXFaceTrackedEffectTransform",&,N) faceTrackingTransform;
@property (TB,R,N) isEmoji;
@property (TB,R,N) hasBackground;
@property (TB,N,GisTextFlipped) flipText;
@property (TB,N,GisTailFlipped) flipTail;
@property (T@"JFXTrackedEffectProperties",&,N,V_trackingProps) trackingProps;
@property (TB,R,N) isTracked;
@property (TB,R,N) isCurrentlyTracking;
@property (TB,N,V_prefersTrackingNotActivateAutomatically) prefersTrackingNotActivateAutomatically;
@property (TB,R,N) isInteractiveEditing;
@property (TB,R,N) isEditingFaceTrackingTransforms;
@property (T@"NSString",C,N) dynamicTextString;
@property (TQ,R,N) dynamicTextType;
```

## Class methods

```
+[JFXOverlayEffect supportsSecureCoding];
+[JFXOverlayEffect dynamicTextPlaceholderMap];
+[JFXOverlayEffect effectIDToImageSequenceIDMap];
```

## Instance methods

```
-[JFXOverlayEffect isHidden];
-[JFXOverlayEffect type];
-[JFXOverlayEffect encodeWithCoder:];
-[JFXOverlayEffect hash];
-[JFXOverlayEffect initWithCoder:];
-[JFXOverlayEffect copyWithZone:];
-[JFXOverlayEffect isEqual:];
-[JFXOverlayEffect hasBackground];
-[JFXOverlayEffect accessibilityName];
-[JFXOverlayEffect isTracked];
-[JFXOverlayEffect isCurrentlyTracking];
-[JFXOverlayEffect imageFrameAtTime:forcePosterFrame:includeDropShadow:relativeTo:basisOrigin:];
-[JFXOverlayEffect JFX_dynamicTextPlaceHolderText];
-[JFXOverlayEffect JFX_hasPosterFrame];
-[JFXOverlayEffect JFX_posterFrameIsCachable];
-[JFXOverlayEffect isEditingFaceTrackingTransforms];
-[JFXOverlayEffect JFX_shouldEnableDynamicLineSpacingForDiacritics];
-[JFXOverlayEffect JFX_stringAtIndex:];
-[JFXOverlayEffect JFX_adjustedMinimumSizeFromNormalizedMinimumSize:atTime:forcePosterFrame:relativeTo:basisOrigin:];
-[JFXOverlayEffect JFX_applyEffectParametersForFaceTrackingTransform:];
-[JFXOverlayEffect accessibilityOverlayEffectLabel];
-[JFXOverlayEffect dynamicTextType];
-[JFXOverlayEffect isEmoji];
-[JFXOverlayEffect JFX_setupTrackingProps];
-[JFXOverlayEffect newPathsForHitTestingAtTime:forcePosterFrame:relativeTo:basisOrigin:adjustForMinimumSize:normalizedMinimumSize:outExpandedPath:];
-[JFXOverlayEffect JFX_updateInteractiveMode];
-[JFXOverlayEffect suspendTracking];
-[JFXOverlayEffect trackedEffectProperties:didChangeTrackingType:didChangeEnabled:];
-[JFXOverlayEffect addTransform:withComponentTime:relativeTo:basisOrigin:];
-[JFXOverlayEffect addTransform:withComponentTime:relativeTo:basisOrigin:restrictToBounds:];
-[JFXOverlayEffect applyScaleToFitFrame:withComponentTime:relativeRect:];
-[JFXOverlayEffect applyScaleToFitFrame:withComponentTime:relativeRect:restrictToBounds:];
-[JFXOverlayEffect beginEditingFaceTrackingTransforms];
-[JFXOverlayEffect beginInteractiveEditing];
-[JFXOverlayEffect closeButtonInset];
-[JFXOverlayEffect contentProperties];
-[JFXOverlayEffect cornersAtTime:forcePosterFrame:includeDropShadow:scale:relativeTo:basisOrigin:];
-[JFXOverlayEffect customPickerRotation];
-[JFXOverlayEffect customPrimaryFillColor];
-[JFXOverlayEffect dynamicTextString];
-[JFXOverlayEffect effectCenterAtTime:forcePosterFrame:includeTransformAnimation:includePlayableAspectScale:relativeTo:basisOrigin:];
-[JFXOverlayEffect effectPointToScreenPoint:effectToScreenTransform:viewSize:];
-[JFXOverlayEffect enablePresentationState:];
-[JFXOverlayEffect endEditingFaceTrackingTransforms];
-[JFXOverlayEffect endInteractiveEditing];
-[JFXOverlayEffect faceTrackingTransform];
-[JFXOverlayEffect hasDynamicText];
-[JFXOverlayEffect hitAreaBoundingFrameAtTime:forcePosterFrame:includeDropShadow:adjustForMinimumSize:normalizedMinimumSize:relativeTo:basisOrigin:];
-[JFXOverlayEffect hitAreaScale];
-[JFXOverlayEffect hitTestPoint:atTime:forcePosterFrame:relativeTo:basisOrigin:adjustForMinimumSize:normalizedMinimumSize:];
-[JFXOverlayEffect includeDropShadowWhenPositioningCloseButton];
-[JFXOverlayEffect initWithEffectID:];
-[JFXOverlayEffect internalFaceTrackingTransform];
-[JFXOverlayEffect isAppearanceEqual:forPurpose:];
-[JFXOverlayEffect isInteractiveEditing];
-[JFXOverlayEffect isTailFlipped];
-[JFXOverlayEffect isTextFlipped];
-[JFXOverlayEffect loopedRangeRenderIsCacheable];
-[JFXOverlayEffect maxCharacters];
-[JFXOverlayEffect objectBounds:time:forcePosterFrame:includeDropShadow:includeMasks:];
-[JFXOverlayEffect osfaToneMappingOption];
-[JFXOverlayEffect overlayContentDataSource];
-[JFXOverlayEffect pickerScale];
-[JFXOverlayEffect prefersTrackingNotActivateAutomatically];
-[JFXOverlayEffect renderEffectWillLoad];
-[JFXOverlayEffect resetDynamicTextString];
-[JFXOverlayEffect resumeTracking];
-[JFXOverlayEffect rotate:aroundPoint:withComponentTime:relativeTo:basisOrigin:];
-[JFXOverlayEffect rotatedAspectRatio];
-[JFXOverlayEffect screenPointToEffectPoint:withComponentTime:relativeTo:basisOrigin:];
-[JFXOverlayEffect serializableEffectParameters];
-[JFXOverlayEffect setAccessibilityOverlayEffectLabel:];
-[JFXOverlayEffect setDynamicTextString:];
-[JFXOverlayEffect setFaceTrackingTransform:];
-[JFXOverlayEffect setFlipTail:];
-[JFXOverlayEffect setFlipText:];
-[JFXOverlayEffect setForceRenderAtPosterFrame:];
-[JFXOverlayEffect setImageSequencePath:];
-[JFXOverlayEffect setImageSequencePathToBundledAssets];
-[JFXOverlayEffect setInternalFaceTrackingTransform:];
-[JFXOverlayEffect setPosition:withComponentTime:relativeTo:basisOrigin:restrictToBounds:];
-[JFXOverlayEffect setPrefersTrackingNotActivateAutomatically:];
-[JFXOverlayEffect setSingleLineScaleThreshold:];
-[JFXOverlayEffect setTrackingProps:];
-[JFXOverlayEffect supportsFlippingTail];
-[JFXOverlayEffect supportsFlippingText];
-[JFXOverlayEffect trackingProps];
-[JFXOverlayEffect transformAtTime:forcePosterFrame:includeTransformAnimation:includePlayableAspectScale:relativeTo:basisOrigin:];
-[JFXOverlayEffect transformAtTime:forcePosterFrame:relativeTo:basisOrigin:];
-[JFXOverlayEffect updateDynamicTextWithCompletionBlock:];
-[JFXOverlayEffect updateRenderSizeMaintainingAppearance:withComponentTime:];
-[JFXOverlayEffect updateRenderSizeMaintainingRelativeSizeAndPosition:toSize:withComponentTime:];
-[JFXOverlayEffect updateRenderSizeMaintainingSizeAndPositionRelativeToMedia:mediaSize:mediaContentMode:];
-[JFXOverlayEffect wasDynamicTextSet];
```
