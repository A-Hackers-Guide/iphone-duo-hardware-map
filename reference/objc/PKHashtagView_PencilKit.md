# `PKHashtagView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKDetectionView`
- 3 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"PKHashtagItem" _hashtagItem;
@"<PKHashtagViewDelegate>" _delegate;
@"UIView" _blankPreviewView;
```

## Properties

```
@property (T@"UIView",&,N,V_blankPreviewView) blankPreviewView;
@property (T@"PKHashtagItem",R,N,V_hashtagItem) hashtagItem;
@property (T@"<PKHashtagViewDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[PKHashtagView contextMenuInteraction:willEndForConfiguration:animator:];
-[PKHashtagView contextMenuInteraction:configurationForMenuAtLocation:];
-[PKHashtagView contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:];
-[PKHashtagView item];
-[PKHashtagView setDelegate:];
-[PKHashtagView accessibilityIdentifier];
-[PKHashtagView delegate];
-[PKHashtagView accessibilityValue];
-[PKHashtagView _underlineColor];
-[PKHashtagView _underlineThickness];
-[PKHashtagView blankPreviewView];
-[PKHashtagView hashtagItem];
-[PKHashtagView initWithHashtagItem:inDrawing:];
-[PKHashtagView setBlankPreviewView:];
-[PKHashtagView updateActivationState];
```
