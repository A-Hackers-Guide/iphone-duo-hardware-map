# `SBPresentationBinderIndirectAccessManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowSceneAttachmentObserving`
- 1 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _binderAccessByDisplayIdentity;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPresentationBinderIndirectAccessManager init];
-[SBPresentationBinderIndirectAccessManager windowSceneDidDisconnect:];
-[SBPresentationBinderIndirectAccessManager dealloc];
-[SBPresentationBinderIndirectAccessManager windowSceneDidConnect:];
-[SBPresentationBinderIndirectAccessManager addScene:toPresentationBinderWithDisplayIdentity:traitsRole:presentingBlock:];
-[SBPresentationBinderIndirectAccessManager currentPresentationBinderForScene:];
-[SBPresentationBinderIndirectAccessManager removeScene:fromPresentationBinderWithDisplayIdentity:dismissingBlock:];
```
