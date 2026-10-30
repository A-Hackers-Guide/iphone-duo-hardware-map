# `SBKeyboardFocusRedirection`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
i _fromProcessIdentifier;
i _toProcessIdentifier;
@"NSString" _reason;
@"FBSSceneIdentityToken" _fromToken;
@"FBSSceneIdentityToken" _toToken;
@"UIWindow" _containingWindow;
```

## Properties

```
@property (T@"NSString",C,N,V_reason) reason;
@property (Ti,N,V_fromProcessIdentifier) fromProcessIdentifier;
@property (T@"FBSSceneIdentityToken",&,N,V_fromToken) fromToken;
@property (Ti,N,V_toProcessIdentifier) toProcessIdentifier;
@property (T@"FBSSceneIdentityToken",&,N,V_toToken) toToken;
@property (T@"BKSHIDEventDeferringTarget",R,N) deferringTarget;
@property (T@"UIWindow",&,N,V_containingWindow) containingWindow;
```

## Instance methods

```
-[SBKeyboardFocusRedirection setReason:];
-[SBKeyboardFocusRedirection description];
-[SBKeyboardFocusRedirection reason];
-[SBKeyboardFocusRedirection setContainingWindow:];
-[SBKeyboardFocusRedirection deferringTarget];
-[SBKeyboardFocusRedirection toToken];
-[SBKeyboardFocusRedirection containingWindow];
-[SBKeyboardFocusRedirection fromProcessIdentifier];
-[SBKeyboardFocusRedirection fromToken];
-[SBKeyboardFocusRedirection setFromProcessIdentifier:];
-[SBKeyboardFocusRedirection setFromToken:];
-[SBKeyboardFocusRedirection setToProcessIdentifier:];
-[SBKeyboardFocusRedirection setToToken:];
-[SBKeyboardFocusRedirection toProcessIdentifier];
```
