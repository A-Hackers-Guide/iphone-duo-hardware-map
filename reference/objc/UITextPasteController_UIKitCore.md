# `UITextPasteController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextPasteCoordinatorDelegate`
- 2 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSMapTable" _sessions;
@"<UITextPasteConfigurationSupporting_Internal>" _supportingView;
```

## Properties

```
@property (T@"<UITextPasteConfigurationSupporting_Internal>",W,N,V_supportingView) supportingView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITextPasteController combineAttributedStrings:addingSeparation:];
```

## Instance methods

```
-[UITextPasteController _restorePasteResultForSession:];
-[UITextPasteController _clampRange:];
-[UITextPasteController _performPasteOfAttributedString:toRange:forSession:completion:];
-[UITextPasteController coordinator:endPastingItems:];
-[UITextPasteController shouldMatchStyleForItem:];
-[UITextPasteController setSupportingView:];
-[UITextPasteController _executePasteForSession:];
-[UITextPasteController beginDroppingItems:toSelectedRange:progressSupport:animated:delegate:];
-[UITextPasteController _combineItemAttributedStrings:forRange:];
-[UITextPasteController supportingView];
-[UITextPasteController beginPastingItems:toRange:];
-[UITextPasteController beginDroppingItems:toSelectedRange:progressSupport:animated:];
-[UITextPasteController beginPastingItems:toRange:delegate:matchesTextStyles:];
-[UITextPasteController _pasteDelegateHandlesPasting];
-[UITextPasteController _transformTextPasteItem:];
-[UITextPasteController initWithSupportingView:];
```
