# `PKProofreadingView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKDetectionView`
- Protocols: `UIEditMenuInteractionDelegate`
- 6 instance variables, 10 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"PKProofreadingItem" _proofreadingItem;
@"<PKProofreadingViewDelegate>" _delegate;
@"UIEditMenuInteraction" _editMenuInteraction;
@"NSTimer" _visibilityTimer;
@"NSMutableSet" _autoHideSuppressionTokens;
@"UIView" _blankPreviewView;
```

## Properties

```
@property (T@"UIEditMenuInteraction",&,N,V_editMenuInteraction) editMenuInteraction;
@property (T@"NSTimer",&,N,V_visibilityTimer) visibilityTimer;
@property (T@"NSMutableSet",&,N,V_autoHideSuppressionTokens) autoHideSuppressionTokens;
@property (T@"UIView",&,N,V_blankPreviewView) blankPreviewView;
@property (T@"PKProofreadingItem",R,N,V_proofreadingItem) proofreadingItem;
@property (T@"<PKProofreadingViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKProofreadingView tapHandler:];
-[PKProofreadingView item];
-[PKProofreadingView editMenuInteraction:willDismissMenuForConfiguration:animator:];
-[PKProofreadingView setDelegate:];
-[PKProofreadingView accessibilityIdentifier];
-[PKProofreadingView editMenuInteraction];
-[PKProofreadingView fadeOut];
-[PKProofreadingView delegate];
-[PKProofreadingView didMoveToSuperview];
-[PKProofreadingView editMenuInteraction:menuForConfiguration:suggestedActions:];
-[PKProofreadingView accessibilityValue];
-[PKProofreadingView setEditMenuInteraction:];
-[PKProofreadingView _underlineColor];
-[PKProofreadingView cancelHideTimer];
-[PKProofreadingView visibilityTimer];
-[PKProofreadingView _setLineDashFor:];
-[PKProofreadingView _underlineThickness];
-[PKProofreadingView allowsAutoHide];
-[PKProofreadingView autoHideSuppressionTokens];
-[PKProofreadingView blankPreviewView];
-[PKProofreadingView ensureViewIsVisible];
-[PKProofreadingView initWithProofreadingItem:inDrawing:];
-[PKProofreadingView popAllAutoHideSuppressionTokensAndFadeOutImmediately];
-[PKProofreadingView popAutoHideSuppressionToken:];
-[PKProofreadingView popAutoHideSuppressionTokens:fadeOutImmediately:];
-[PKProofreadingView proofreadingItem];
-[PKProofreadingView pushAutoHideSuppressionToken:forceShow:];
-[PKProofreadingView setAutoHideSuppressionTokens:];
-[PKProofreadingView setBlankPreviewView:];
-[PKProofreadingView setVisibilityTimer:];
-[PKProofreadingView startHideTimer];
```
