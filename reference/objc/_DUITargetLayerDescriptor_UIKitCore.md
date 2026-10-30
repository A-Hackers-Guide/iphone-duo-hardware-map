# `_DUITargetLayerDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
I _contextID;
I _setDownAnimationContextID;
Q _renderID;
@"NSString" _systemShellHostingSpaceIdentifier;
Q _setDownAnimationRenderID;
```

## Properties

```
@property (TI,N,V_contextID) contextID;
@property (TQ,N,V_renderID) renderID;
@property (T@"NSString",C,N,V_systemShellHostingSpaceIdentifier) systemShellHostingSpaceIdentifier;
@property (TI,N,V_setDownAnimationContextID) setDownAnimationContextID;
@property (TQ,N,V_setDownAnimationRenderID) setDownAnimationRenderID;
```

## Class methods

```
+[_DUITargetLayerDescriptor supportsSecureCoding];
```

## Instance methods

```
-[_DUITargetLayerDescriptor systemShellHostingSpaceIdentifier];
-[_DUITargetLayerDescriptor setContextID:];
-[_DUITargetLayerDescriptor setSystemShellHostingSpaceIdentifier:];
-[_DUITargetLayerDescriptor encodeWithCoder:];
-[_DUITargetLayerDescriptor hash];
-[_DUITargetLayerDescriptor initWithCoder:];
-[_DUITargetLayerDescriptor contextID];
-[_DUITargetLayerDescriptor copyWithZone:];
-[_DUITargetLayerDescriptor isEqual:];
-[_DUITargetLayerDescriptor renderID];
-[_DUITargetLayerDescriptor setDownAnimationContextID];
-[_DUITargetLayerDescriptor setDownAnimationRenderID];
-[_DUITargetLayerDescriptor setRenderID:];
-[_DUITargetLayerDescriptor setSetDownAnimationContextID:];
-[_DUITargetLayerDescriptor setSetDownAnimationRenderID:];
```
