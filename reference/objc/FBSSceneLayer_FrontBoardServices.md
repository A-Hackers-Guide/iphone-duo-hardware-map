# `FBSSceneLayer`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"CAContext" _context;
I _contextID;
Q _renderID;
d _level;
@"FBSSceneIdentityToken" _keyboardOwner;
q _type;
q _alignment;
@"NSString" _stringRepresentation;
```

## Properties

```
@property (T@"CAContext",R,N) CAContext;
@property (Td,R,N) level;
@property (TI,R,N) contextID;
@property (TQ,R,N) renderID;
@property (T@"FBSSceneIdentityToken",R,N) keyboardOwner;
@property (Tq,R,N) type;
@property (Tq,R,N) alignment;
```

## Instance methods

```
-[FBSSceneLayer keyboardOwner];
-[FBSSceneLayer init];
-[FBSSceneLayer initWithKeyboardOwner:level:];
-[FBSSceneLayer dealloc];
-[FBSSceneLayer level];
-[FBSSceneLayer _init];
-[FBSSceneLayer alignment];
-[FBSSceneLayer isKeyboardLayer];
-[FBSSceneLayer type];
-[FBSSceneLayer stringRepresentation];
-[FBSSceneLayer hash];
-[FBSSceneLayer description];
-[FBSSceneLayer isKindOfClass:];
-[FBSSceneLayer contextID];
-[FBSSceneLayer isCAContextLayer];
-[FBSSceneLayer CAContext];
-[FBSSceneLayer initWithContextID:renderID:level:];
-[FBSSceneLayer initWithWindowContext:];
-[FBSSceneLayer isEqual:];
-[FBSSceneLayer initWithKeyboardContext:];
-[FBSSceneLayer isKeyboardProxyLayer];
-[FBSSceneLayer renderID];
-[FBSSceneLayer capture];
```
