# `PKDataDetectorInteractionHelper`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKHashtagViewDelegate`, `PKMentionViewDelegate`, `PKProofreadingViewDelegate`
- 27 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _shouldHideItems;
B _wantsDataDetection;
B _wantsProofreadingDetection;
B _ignoreInitialDetectionItemsForStatistics;
B _deferMentionUpdate;
B _detectionViewsHidden;
B _wantsHashtagDetection;
B _wantsMentionDetection;
B _isDraggingSelection;
B _toolPickerVisible;
B _hideUntilScroll;
@"<PKDataDetectorInteractionHelperDelegate>" _delegate;
@"UIView" _view;
@"UIView" _parentView;
@"PKRecognitionController" _recogntionController;
@"NSMutableArray" _dataDetectorViews;
@"NSMutableArray" _mentionViews;
@"NSMutableArray" _hashtagViews;
@"NSMutableArray" _proofreadingViews;
@"NSMutableArray" _previousDataDetectorItems;
@"NSMutableArray" _previousHashtagItems;
@"NSMutableArray" _previousMentionItems;
@"NSMutableArray" _previousProofreadingItems;
@"NSMutableDictionary" _mentionUUIDtoParticipant;
@"<PKAttachmentViewHashtagsAndMentionsDelegate>" _hashtagAndMentionsDelegate;
@"PKAttachmentView" _attachmentView;
@"UIView" _proofreadingContainerView;
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
-[PKDataDetectorInteractionHelper _accessibilityUserTestingChildren];
-[PKDataDetectorInteractionHelper hashtagView:registerCommand:];
-[PKDataDetectorInteractionHelper hashtagViewDidActivateHashtag:];
-[PKDataDetectorInteractionHelper hashtagViewDidDeactivateHashtag:];
-[PKDataDetectorInteractionHelper hashtagViewWillDeactivateHashtag:];
-[PKDataDetectorInteractionHelper mentionView:registerCommand:];
-[PKDataDetectorInteractionHelper mentionViewDidActivateMention:withParticpant:];
-[PKDataDetectorInteractionHelper mentionViewDidDeactivateMention:];
-[PKDataDetectorInteractionHelper mentionViewWillDeactivateMention:];
-[PKDataDetectorInteractionHelper proofreadingView:didReplaceWithString:];
-[PKDataDetectorInteractionHelper proofreadingView:willDismissStringsForProofreadingItem:];
-[PKDataDetectorInteractionHelper proofreadingView:willPresentStringsForProofreadingItem:];
-[PKDataDetectorInteractionHelper revealDetectionViews];
```
