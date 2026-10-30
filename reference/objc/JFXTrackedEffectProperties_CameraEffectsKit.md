# `JFXTrackedEffectProperties`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _disableTracking;
@"<JFXTrackedEffectPropertiesDelegate>" _delegate;
q _internalTrackingType;
```

## Properties

```
@property (Tq,V_internalTrackingType) internalTrackingType;
@property (TB,GisTrackingDisabled,V_disableTracking) disableTracking;
@property (Tq,N) trackingType;
@property (Tq,R,N) currentTrackingType;
@property (T@"<JFXTrackedEffectPropertiesDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[JFXTrackedEffectProperties supportsSecureCoding];
```

## Instance methods

```
-[JFXTrackedEffectProperties init];
-[JFXTrackedEffectProperties setDelegate:];
-[JFXTrackedEffectProperties encodeWithCoder:];
-[JFXTrackedEffectProperties delegate];
-[JFXTrackedEffectProperties initWithCoder:];
-[JFXTrackedEffectProperties copyWithZone:];
-[JFXTrackedEffectProperties setTrackingType:];
-[JFXTrackedEffectProperties trackingType];
-[JFXTrackedEffectProperties currentTrackingType];
-[JFXTrackedEffectProperties enableTrackingState:];
-[JFXTrackedEffectProperties internalTrackingType];
-[JFXTrackedEffectProperties isTrackingDisabled];
-[JFXTrackedEffectProperties setDisableTracking:];
-[JFXTrackedEffectProperties setInternalTrackingType:];
```
