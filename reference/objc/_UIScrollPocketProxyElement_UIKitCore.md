# `_UIScrollPocketProxyElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BSXPCCoding`
- 5 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
Q _edge;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frameInSceneCoordinateSpace;
B _requiresPocket;
@"NSString" _identifier;
q _style;
```

## Properties

```
@property (TB,R,N) hasValidFrame;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (Tq,R,N,V_style) style;
@property (TQ,R,N,V_edge) edge;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIScrollPocketProxyElement initWithEdge:];
-[_UIScrollPocketProxyElement debugDescription];
-[_UIScrollPocketProxyElement edge];
-[_UIScrollPocketProxyElement identifier];
-[_UIScrollPocketProxyElement initWithXPCDictionary:];
-[_UIScrollPocketProxyElement updateWithFrameInSceneCoordinateSpace:style:];
-[_UIScrollPocketProxyElement style];
-[_UIScrollPocketProxyElement succinctDescription];
-[_UIScrollPocketProxyElement updateWithElement:coordinateSpace:];
-[_UIScrollPocketProxyElement encodeWithXPCDictionary:];
-[_UIScrollPocketProxyElement description];
-[_UIScrollPocketProxyElement updateInteraction:];
-[_UIScrollPocketProxyElement appendDescriptionToStream:];
-[_UIScrollPocketProxyElement copyWithZone:];
-[_UIScrollPocketProxyElement hasValidFrame];
-[_UIScrollPocketProxyElement isEqual:];
```
