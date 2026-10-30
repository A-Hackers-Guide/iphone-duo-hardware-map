# `_UIOServerActionOriginContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSMutableCopying`, `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"NSString" _sceneIdentity;
@"NSString" _spaceIdentifier;
I _contextId;
Q _layerId;
{CGPoint="x"d"y"d} _layerReferencePoint;
```

## Properties

```
@property (T@"NSString",R,C,N,V_sceneIdentity) sceneIdentity;
@property (T@"NSString",R,C,N,V_spaceIdentifier) spaceIdentifier;
@property (TI,R,N,V_contextId) contextId;
@property (TQ,R,N,V_layerId) layerId;
@property (T{CGPoint=dd},R,N,V_layerReferencePoint) layerReferencePoint;
```

## Class methods

```
+[_UIOServerActionOriginContext supportsSecureCoding];
+[_UIOServerActionOriginContext defaultOriginContext];
+[_UIOServerActionOriginContext originContextForView:referencePoint:];
```

## Instance methods

```
-[_UIOServerActionOriginContext contextId];
-[_UIOServerActionOriginContext mutableCopyWithZone:];
-[_UIOServerActionOriginContext sceneIdentity];
-[_UIOServerActionOriginContext encodeWithCoder:];
-[_UIOServerActionOriginContext description];
-[_UIOServerActionOriginContext initWithCoder:];
-[_UIOServerActionOriginContext copyWithZone:];
-[_UIOServerActionOriginContext layerId];
-[_UIOServerActionOriginContext spaceIdentifier];
-[_UIOServerActionOriginContext _configureWithWindow:];
-[_UIOServerActionOriginContext layerReferencePoint];
-[_UIOServerActionOriginContext translatedReferencePointForDestinationView:];
```
