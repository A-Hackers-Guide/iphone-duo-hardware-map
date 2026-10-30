# `FBSceneLayer`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`
- 6 instance variables, 12 properties, 23 instance methods, 1 class methods

## Instance variables

```
q _type;
d _level;
q _alignment;
I _contextID;
Q _renderID;
@"FBSSceneIdentityToken" _proxiedKeyboardOwner;
```

## Properties

```
@property (Td,N,V_level) level;
@property (Tq,N,V_alignment) alignment;
@property (TB,R,N) isKeyboardLayer;
@property (TB,R,N) isKeyboardProxyLayer;
@property (Tq,R,N,V_type) type;
@property (TI,R,N,V_contextID) contextID;
@property (TQ,R,N,V_renderID) renderID;
@property (T@"FBSSceneIdentityToken",R,C,N,V_proxiedKeyboardOwner) proxiedKeyboardOwner;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSceneLayer layerWithFBSSceneLayer:];
```

## Instance methods

```
-[FBSceneLayer succinctDescriptionBuilder];
-[FBSceneLayer init];
-[FBSceneLayer level];
-[FBSceneLayer setAlignment:];
-[FBSceneLayer descriptionWithMultilinePrefix:];
-[FBSceneLayer alignment];
-[FBSceneLayer succinctDescription];
-[FBSceneLayer setLevel:];
-[FBSceneLayer isKeyboardLayer];
-[FBSceneLayer type];
-[FBSceneLayer hash];
-[FBSceneLayer description];
-[FBSceneLayer contextID];
-[FBSceneLayer copyWithZone:];
-[FBSceneLayer isEqual:];
-[FBSceneLayer isKeyboardProxyLayer];
-[FBSceneLayer renderID];
-[FBSceneLayer descriptionBuilderWithMultilinePrefix:];
-[FBSceneLayer proxiedKeyboardOwner];
-[FBSceneLayer externalSceneID];
-[FBSceneLayer initAsKeyboard];
-[FBSceneLayer initAsKeyboardProxyWithOwner:];
-[FBSceneLayer initWithContextID:renderID:];
```
