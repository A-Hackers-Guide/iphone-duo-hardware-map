# `_UISheetPresentationControllerClientConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSXPCSecureCoding`
- 4 instance variables, 8 properties, 14 instance methods, 2 class methods

## Instance variables

```
B _containsFirstResponder;
B _firstResponderRequiresKeyboard;
d _proposedDepthLevel;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyboardFrame;
```

## Properties

```
@property (TB,N,V_containsFirstResponder) containsFirstResponder;
@property (TB,N,V_firstResponderRequiresKeyboard) firstResponderRequiresKeyboard;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_keyboardFrame) keyboardFrame;
@property (Td,N,V_proposedDepthLevel) proposedDepthLevel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISheetPresentationControllerClientConfiguration supportsBSXPCSecureCoding];
+[_UISheetPresentationControllerClientConfiguration supportsSecureCoding];
```

## Instance methods

```
-[_UISheetPresentationControllerClientConfiguration setProposedDepthLevel:];
-[_UISheetPresentationControllerClientConfiguration keyboardFrame];
-[_UISheetPresentationControllerClientConfiguration setFirstResponderRequiresKeyboard:];
-[_UISheetPresentationControllerClientConfiguration firstResponderRequiresKeyboard];
-[_UISheetPresentationControllerClientConfiguration setKeyboardFrame:];
-[_UISheetPresentationControllerClientConfiguration encodeWithCoder:];
-[_UISheetPresentationControllerClientConfiguration containsFirstResponder];
-[_UISheetPresentationControllerClientConfiguration description];
-[_UISheetPresentationControllerClientConfiguration initWithCoder:];
-[_UISheetPresentationControllerClientConfiguration encodeWithBSXPCCoder:];
-[_UISheetPresentationControllerClientConfiguration initWithBSXPCCoder:];
-[_UISheetPresentationControllerClientConfiguration isEqual:];
-[_UISheetPresentationControllerClientConfiguration proposedDepthLevel];
-[_UISheetPresentationControllerClientConfiguration setContainsFirstResponder:];
```
