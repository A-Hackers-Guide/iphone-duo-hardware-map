# `UIPressAndHoldPopoverController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardPopoverController`
- Protocols: `TUIPressAndHoldViewDelegate`
- 1 instance variables, 4 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"TUIPressAndHoldView" _pressAndHoldView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPressAndHoldPopoverController canPresentPressAndHoldPopoverForEvent:];
+[UIPressAndHoldPopoverController canPresentPressAndHoldPopoverForKeyString:];
```

## Instance methods

```
-[UIPressAndHoldPopoverController handleHardwareKeyboardEvent:];
-[UIPressAndHoldPopoverController handleKeyInputForAccentSelector:];
-[UIPressAndHoldPopoverController handleKeyInputForPressAndHoldSelector:];
-[UIPressAndHoldPopoverController handleSelectionEvent:];
-[UIPressAndHoldPopoverController hasAccentVariantInForwardDirection:];
-[UIPressAndHoldPopoverController initWithKeyString:];
-[UIPressAndHoldPopoverController insertSelectedAccentVariant:shouldDismissPopover:];
-[UIPressAndHoldPopoverController isSamePressAndHoldPopoverForKeyString:];
-[UIPressAndHoldPopoverController pressAndHoldViewDidAcceptAccentVariant:atIndexPath:];
-[UIPressAndHoldPopoverController showAccentVariantInForwardDirection:];
```
