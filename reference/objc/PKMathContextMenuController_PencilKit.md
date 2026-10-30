# `PKMathContextMenuController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIContextMenuInteractionDelegate_ForWebKitOnly`, `UIContextMenuInteractionDelegate_Private`
- 12 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
B _supportCopy;
B _graphAddtoExisting;
@"UIContextMenuInteraction" _interaction;
@"PKMathRecognitionItem" _mathItem;
@"PKMathRecognitionToken" _mathToken;
@"UIView" _view;
@"<PKMathContextMenuControllerDelegate>" _delegate;
q _mode;
@"NSString" _explanationString;
@"NSString" _errorString;
@"NSString" _errorReasonString;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _tapBounds;
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
-[PKMathContextMenuController contextMenuInteraction:willEndForConfiguration:animator:];
-[PKMathContextMenuController contextMenuInteraction:configurationForMenuAtLocation:];
-[PKMathContextMenuController contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:];
-[PKMathContextMenuController _contextMenuInteraction:overrideSuggestedActionsForConfiguration:];
```
