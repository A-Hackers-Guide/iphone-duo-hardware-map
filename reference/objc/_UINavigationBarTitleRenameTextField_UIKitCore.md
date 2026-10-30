# `_UINavigationBarTitleRenameTextField`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextField`
- Protocols: `_UIPassthroughScrollInteractionDelegate`, `_UINavigationBarTitleRenamerContentView`
- 5 instance variables, 11 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"FBSSceneIdentityToken" _layeringSceneIdentity;
@? _horizontalTextInsetDidChangeCallback;
@"_UINavigationBarTitleRenamerSession" _session;
@"NSLayoutConstraint" _iconHeightConstraint;
@"_UIPassthroughScrollInteraction" _passthroughInteraction;
```

## Properties

```
@property (T@"_UINavigationBarTitleRenamerSession",R,N,V_session) session;
@property (T@"NSLayoutConstraint",R,N,V_iconHeightConstraint) iconHeightConstraint;
@property (T@"_UIPassthroughScrollInteraction",&,N,V_passthroughInteraction) passthroughInteraction;
@property (T@"FBSSceneIdentityToken",&,N,S_setLayeringSceneIdentity:,V_layeringSceneIdentity) _layeringSceneIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N) textAlignment;
@property (Td,R,N) horizontalTextInset;
@property (T@?,C,N,V_horizontalTextInsetDidChangeCallback) horizontalTextInsetDidChangeCallback;
```

## Instance methods

```
-[_UINavigationBarTitleRenameTextField didMoveToWindow];
-[_UINavigationBarTitleRenameTextField layoutSubviews];
-[_UINavigationBarTitleRenameTextField passthroughScrollInteractionDidRecognize:atLocation:];
-[_UINavigationBarTitleRenameTextField passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UINavigationBarTitleRenameTextField willMoveToWindow:];
-[_UINavigationBarTitleRenameTextField canResignFirstResponder];
-[_UINavigationBarTitleRenameTextField initWithSession:];
-[_UINavigationBarTitleRenameTextField session];
-[_UINavigationBarTitleRenameTextField _becomeFirstResponder];
-[_UINavigationBarTitleRenameTextField _layeringSceneIdentity];
-[_UINavigationBarTitleRenameTextField _resignFirstResponder];
-[_UINavigationBarTitleRenameTextField _setLayeringSceneIdentity:];
-[_UINavigationBarTitleRenameTextField _setupIconViewIfNecessary];
-[_UINavigationBarTitleRenameTextField _shouldEndEditingOnReturn];
-[_UINavigationBarTitleRenameTextField horizontalTextInset];
-[_UINavigationBarTitleRenameTextField horizontalTextInsetDidChangeCallback];
-[_UINavigationBarTitleRenameTextField iconHeightConstraint];
-[_UINavigationBarTitleRenameTextField passthroughInteraction];
-[_UINavigationBarTitleRenameTextField setHorizontalTextInsetDidChangeCallback:];
-[_UINavigationBarTitleRenameTextField setPassthroughInteraction:];
-[_UINavigationBarTitleRenameTextField supportsImagePaste];
```
