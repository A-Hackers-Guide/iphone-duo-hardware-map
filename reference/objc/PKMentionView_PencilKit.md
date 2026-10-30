# `PKMentionView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKDetectionView`
- 5 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"PKMentionItem" _mentionItem;
@"UIColor" _mentionColor;
@"<PKMentionViewDelegate>" _delegate;
@"UIView" _blankPreviewView;
@"NSArray" _possibleParticipants;
```

## Properties

```
@property (T@"UIView",&,N,V_blankPreviewView) blankPreviewView;
@property (T@"NSArray",C,N,V_possibleParticipants) possibleParticipants;
@property (T@"PKMentionItem",R,N,V_mentionItem) mentionItem;
@property (T@"UIColor",&,N,V_mentionColor) mentionColor;
@property (T@"<PKMentionViewDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[PKMentionView contextMenuInteraction:willEndForConfiguration:animator:];
-[PKMentionView contextMenuInteraction:configurationForMenuAtLocation:];
-[PKMentionView contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:];
-[PKMentionView item];
-[PKMentionView setDelegate:];
-[PKMentionView accessibilityIdentifier];
-[PKMentionView delegate];
-[PKMentionView accessibilityValue];
-[PKMentionView _underlineColor];
-[PKMentionView _underlineThickness];
-[PKMentionView blankPreviewView];
-[PKMentionView initWithMentionItem:possibleParticipants:inDrawing:];
-[PKMentionView mentionColor];
-[PKMentionView mentionItem];
-[PKMentionView possibleParticipants];
-[PKMentionView setBlankPreviewView:];
-[PKMentionView setMentionColor:];
-[PKMentionView setPossibleParticipants:];
-[PKMentionView updateActivationState];
```
