# `UITextDropRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"UITextPosition",R,N) dropPosition;
@property (T@"UITextDropProposal",R,N) suggestedProposal;
@property (TB,R,N,GisSameView) sameView;
@property (T@"<UIDropSession>",R,N) dropSession;
```

## Instance methods

```
-[UITextDropRequest dropSession];
-[UITextDropRequest dropPosition];
-[UITextDropRequest isSameView];
-[UITextDropRequest suggestedProposal];
```
