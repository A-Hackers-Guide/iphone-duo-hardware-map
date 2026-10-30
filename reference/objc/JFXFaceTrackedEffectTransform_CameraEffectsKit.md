# `JFXFaceTrackedEffectTransform`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _effectParametersForOnFaceTracking;
@"NSDictionary" _effectParametersForOnBillboardTracking;
{?="columns"[4]} _cameraProjection;
{?="columns"[4]} _cameraTransform;
{?="columns"[4]} _billboardTransform;
{?="columns"[4]} _onFaceTransform;
```

## Properties

```
@property (T{?=[4]},R,N,V_cameraProjection) cameraProjection;
@property (T{?=[4]},R,N,V_cameraTransform) cameraTransform;
@property (T{?=[4]},R,N,V_billboardTransform) billboardTransform;
@property (T{?=[4]},R,N,V_onFaceTransform) onFaceTransform;
@property (T@"NSDictionary",R,N,V_effectParametersForOnFaceTracking) effectParametersForOnFaceTracking;
@property (T@"NSDictionary",R,N,V_effectParametersForOnBillboardTracking) effectParametersForOnBillboardTracking;
```

## Instance methods

```
-[JFXFaceTrackedEffectTransform copyWithZone:];
-[JFXFaceTrackedEffectTransform cameraTransform];
-[JFXFaceTrackedEffectTransform onFaceTransform];
-[JFXFaceTrackedEffectTransform billboardTransform];
-[JFXFaceTrackedEffectTransform cameraProjection];
-[JFXFaceTrackedEffectTransform effectParametersForOnBillboardTracking];
-[JFXFaceTrackedEffectTransform effectParametersForOnFaceTracking];
-[JFXFaceTrackedEffectTransform effectParametersForTrackingType:];
-[JFXFaceTrackedEffectTransform initWithCameraProjection:cameraTransform:onFaceTransform:billboardTransform:];
-[JFXFaceTrackedEffectTransform isEqual:forTrackingType:];
-[JFXFaceTrackedEffectTransform transformForTrackingType:];
```
