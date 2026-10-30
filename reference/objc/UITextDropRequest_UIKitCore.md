# `UITextDropRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextDropRequest_Private`, `UITextDropRequest`
- 5 instance variables, 9 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _sameView;
@"<UIDropSession>" _dropSession;
@"UITextPosition" _dropPosition;
@"UITextRange" _dropRange;
@"UITextDropProposal" _suggestedProposal;
```

## Properties

```
@property (T@"UITextDropProposal",&,N,V_suggestedProposal) suggestedProposal;
@property (TB,N,GisSameView,V_sameView) sameView;
@property (T@"UITextRange",R,N,V_dropRange) dropRange;
@property (T@"UITextPosition",R,N,V_dropPosition) dropPosition;
@property (T@"<UIDropSession>",R,N,V_dropSession) dropSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextDropRequest dropSession];
-[UITextDropRequest dropPosition];
-[UITextDropRequest dropRange];
-[UITextDropRequest initWithPosition:range:inSession:];
-[UITextDropRequest isSameView];
-[UITextDropRequest setSameView:];
-[UITextDropRequest setSuggestedProposal:];
-[UITextDropRequest suggestedProposal];
```
