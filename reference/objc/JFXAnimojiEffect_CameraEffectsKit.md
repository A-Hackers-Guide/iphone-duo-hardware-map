# `JFXAnimojiEffect`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXEffect`
- 1 instance variables, 2 properties, 19 instance methods, 5 class methods

## Instance variables

```
q _captureInterfaceOrientation;
```

## Properties

```
@property (T@"UIImage",R,N) thumbnail;
@property (Tq,N,V_captureInterfaceOrientation) captureInterfaceOrientation;
```

## Class methods

```
+[JFXAnimojiEffect supportsSecureCoding];
+[JFXAnimojiEffect animojiIDs];
+[JFXAnimojiEffect createAnimojiEffectForID:];
+[JFXAnimojiEffect createMemojiEffectWithContentsOfFile:identifier:];
+[JFXAnimojiEffect isAvatarKitAvailable];
```

## Instance methods

```
-[JFXAnimojiEffect dataRepresentation];
-[JFXAnimojiEffect displayName];
-[JFXAnimojiEffect type];
-[JFXAnimojiEffect encodeWithCoder:];
-[JFXAnimojiEffect thumbnail];
-[JFXAnimojiEffect initWithCoder:];
-[JFXAnimojiEffect copyWithZone:];
-[JFXAnimojiEffect renderEffect];
-[JFXAnimojiEffect _convertRenderEffectPoints:numPoints:fromBasisRect:basisOrigin:];
-[JFXAnimojiEffect setCaptureInterfaceOrientation:];
-[JFXAnimojiEffect _affineTransformFromEffectRect:toSize:basisOrigin:];
-[JFXAnimojiEffect _convertRenderEffectPoints:numPoints:toBasisRect:basisOrigin:];
-[JFXAnimojiEffect _convertRenderEffectPoints:toBasisRect:basisOrigin:];
-[JFXAnimojiEffect avatarVersionNumber];
-[JFXAnimojiEffect captureInterfaceOrientation];
-[JFXAnimojiEffect loadRenderEffect];
-[JFXAnimojiEffect loadRenderEffectInBackgroundWithCompletionOnMainQueue:];
-[JFXAnimojiEffect loadRenderEffectOnQueue:completion:];
-[JFXAnimojiEffect transform:basisOrigin:];
```
