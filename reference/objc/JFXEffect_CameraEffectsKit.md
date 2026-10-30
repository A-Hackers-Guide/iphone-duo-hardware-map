# `JFXEffect`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXEffectAssetProviderProtocol`, `JFXEffectPreviewAssetProviderProtocol`, `JFXEffectRenderingAssetProviderProtocol`, `NSSecureCoding`, `NSCopying`
- 10 instance variables, 28 properties, 99 instance methods, 4 class methods

## Instance variables

```
@"NSString" _effectID;
i _type;
@"PVEffect" _renderEffect;
@"NSMutableDictionary" _effectParameters;
@"NSMutableDictionary" _dirtyEffectParameters;
@"NSLock" _paramLock;
B _isNone;
@"<JFXEffectContentDataSource>" _contentDataSource;
@"NSString" _motionDocumentFolderPath;
{CGSize="width"d"height"d} _renderSize;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) arePreviewingAssetsLocal;
@property (TB,R,N) areRenderingAssetsLocal;
@property (Td,N) outputAspect;
@property (T@"NSString",R,N,V_effectID) effectID;
@property (TB,R,N,V_isNone) isNone;
@property (Ti,R,N) type;
@property (Tf,N) opacity;
@property (TB,N,GisHidden) hidden;
@property (T@"<JFXEffectContentDataSource>",R,N,V_contentDataSource) contentDataSource;
@property (TQ,R,N) contentAvailability;
@property (TB,R,N) isContentAvailable;
@property (TB,R,N) isContentNew;
@property (T@"NSString",R,N) contentVersion;
@property (TB) forceRenderAtPosterFrame;
@property (T{CGSize=dd},N,V_renderSize) renderSize;
@property (Tq,N) playableAspectRatio;
@property (Tq,N) playableAspectRatioPreservationMode;
@property (T@"NSString",C,N,V_motionDocumentFolderPath) motionDocumentFolderPath;
@property (T@"NSDictionary",C,N) effectParameters;
@property (TB) forceDisableLooping;
@property (TB,R,N) renderEffectResourcesAreReady;
@property (T@"PVMatrix44Double",&,N) topLevelTransformObject;
@property (T{?=[4]},N) topLevelTransform;
@property (T@"PVTransformAnimation",&,N) transformAnimation;
```

## Class methods

```
+[JFXEffect supportsSecureCoding];
+[JFXEffect effectIDIsNone:];
+[JFXEffect defaultPlayableAspectRatio];
+[JFXEffect defaultPlayableAspectRatioPreservationMode];
```

## Instance methods

```
-[JFXEffect renderSize];
-[JFXEffect setHidden:];
-[JFXEffect contentVersion];
-[JFXEffect displayName];
-[JFXEffect dealloc];
-[JFXEffect opacity];
-[JFXEffect setOpacity:];
-[JFXEffect isHidden];
-[JFXEffect type];
-[JFXEffect encodeWithCoder:];
-[JFXEffect hash];
-[JFXEffect description];
-[JFXEffect initWithCoder:];
-[JFXEffect copyWithZone:];
-[JFXEffect isEqual:];
-[JFXEffect accessibilityName];
-[JFXEffect parameterForKey:];
-[JFXEffect setParameter:forKey:];
-[JFXEffect effectParameters];
-[JFXEffect removeEffectParameters:];
-[JFXEffect setEffectParameters:];
-[JFXEffect setRenderSize:];
-[JFXEffect isNone];
-[JFXEffect transformAnimation];
-[JFXEffect effectID];
-[JFXEffect isContentAvailable];
-[JFXEffect renderEffect];
-[JFXEffect _convertRenderEffectPoints:numPoints:fromBasisRect:basisOrigin:];
-[JFXEffect JFX_defaultMotionDocumentFolderLocalURL];
-[JFXEffect setHDR:];
-[JFXEffect _affineTransformFromEffectRect:toSize:basisOrigin:];
-[JFXEffect _convertRenderEffectPoints:numPoints:toBasisRect:basisOrigin:];
-[JFXEffect _convertRenderEffectPoints:toBasisRect:basisOrigin:];
-[JFXEffect _createCachedRenderEffect_noLock];
-[JFXEffect addEffectParameters:];
-[JFXEffect addTransform:withComponentTime:relativeTo:basisOrigin:];
-[JFXEffect addTransform:withComponentTime:relativeTo:basisOrigin:ignoreTranslation:];
-[JFXEffect arePreviewingAssetsLocal];
-[JFXEffect areRenderingAssetsLocal];
-[JFXEffect availableAssetsWithFilteringOptions:];
-[JFXEffect availableAssetsWithFilteringOptionsArray:];
-[JFXEffect buildInAnimation];
-[JFXEffect cancelAssetRequest:];
-[JFXEffect contentAvailability];
-[JFXEffect contentDataSource];
-[JFXEffect contentProperties];
-[JFXEffect describeRequest:];
-[JFXEffect effectWillRenderPreviewWithOptions:];
-[JFXEffect enablePresentationState:];
-[JFXEffect forceDisableLooping];
-[JFXEffect forceRenderAtPosterFrame];
-[JFXEffect initWithEffectID:];
-[JFXEffect isAppearanceEqual:];
-[JFXEffect isAppearanceEqual:forPurpose:];
-[JFXEffect isConfiguredForOutputAspect:];
-[JFXEffect isConfiguredForOutputAspectMatchingSize:];
-[JFXEffect isContentNew];
-[JFXEffect loadRenderEffect];
-[JFXEffect loadRenderEffectInBackgroundWithCompletionOnMainQueue:];
-[JFXEffect loadRenderEffectOnQueue:completion:];
-[JFXEffect localAssetsWithFilteringOptions:];
-[JFXEffect loopedRangeRenderIsCacheable];
-[JFXEffect motionDocumentFolderPath];
-[JFXEffect outputAspect];
-[JFXEffect parametersClassWhitelist];
-[JFXEffect playableAspectRatio];
-[JFXEffect playableAspectRatioPreservationMode];
-[JFXEffect playableRectInOutputSize:];
-[JFXEffect playableScaleInOutputSize:];
-[JFXEffect rangeForPresentationRange:];
-[JFXEffect registerMotionDocumentWithinAssets:];
-[JFXEffect removeTopLevelAdditionalScale];
-[JFXEffect renderEffectResourcesAreReady];
-[JFXEffect renderEffectWillLoad];
-[JFXEffect requestAllAssetsWithOptions:progressAndCancellationHandler:completionHandler:];
-[JFXEffect requestAllAssetsWithOptions:progressHandler:completionHandler:];
-[JFXEffect requestAssetWithOptions:progressAndCancellationHandler:completionHandler:];
-[JFXEffect requestAssetWithOptions:progressHandler:completionHandler:];
-[JFXEffect requestPreviewingAssetsWithPriority:onlyThumbnailAssetWhenAvailable:progressHandler:completionHandler:];
-[JFXEffect requestRenderingAssetsWithPriority:progressHandler:completionHandler:];
-[JFXEffect serializableEffectParameters];
-[JFXEffect setBuildInAnimation:];
-[JFXEffect setForceDisableLooping:];
-[JFXEffect setForceRenderAtPosterFrame:];
-[JFXEffect setMotionDocumentFolderPath:];
-[JFXEffect setOutputAspect:];
-[JFXEffect setParentTransformAnimation:];
-[JFXEffect setPlayableAspectRatio:];
-[JFXEffect setPlayableAspectRatioPreservationMode:];
-[JFXEffect setRenderStartOffset:];
-[JFXEffect setTopLevelAdditionalScale:];
-[JFXEffect setTopLevelTransform:];
-[JFXEffect setTopLevelTransform:relativeTo:basisOrigin:];
-[JFXEffect setTopLevelTransformObject:];
-[JFXEffect setTransformAnimation:];
-[JFXEffect topLevelTransform];
-[JFXEffect topLevelTransformObject];
-[JFXEffect topLevelTransformRelativeTo:basisOrigin:];
-[JFXEffect updatePriorityForAssetRequest:newPriority:];
```
