# `UITextDropSupporting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UITextDroppable`, `UITextPasteConfigurationSupporting`
- 0 instance variables, 1 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T{CGPoint=dd},?,N) contentOffsetForSameViewDrops;
```

## Instance methods

```
-[UITextDropSupporting allowsEditingTextAttributes];
-[UITextDropSupporting droppingStarted];
-[UITextDropSupporting becomeDropResponder];
-[UITextDropSupporting canBecomeDropResponder];
-[UITextDropSupporting droppingFinished];
-[UITextDropSupporting resignDropResponderWithDropPerformed:];
-[UITextDropSupporting _attributedStringForInsertionOfAttributedString:];
-[UITextDropSupporting contentOffsetForSameViewDrops];
-[UITextDropSupporting sanitizeAttributedText:];
-[UITextDropSupporting setContentOffsetForSameViewDrops:];
```
