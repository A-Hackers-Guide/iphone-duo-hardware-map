# `UIKeyboardEmojiCollectionInputView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardEmojiKeyView`
- Protocols: `UIKeyboardMediaControllerDelegate`, `UICollectionViewDataSource`, `UICollectionViewDelegate`, `TUIEmojiSearchInputViewControllerDelegate`
- 24 instance variables, 14 properties, 94 instance methods, 2 class methods

## Instance variables

```
@"UIKeyboardEmojiCollectionView" _collectionView;
@"UICollectionViewFlowLayout" _flowLayout;
@"UIKeyboardEmojiGraphicsTraits" _emojiGraphicsTraits;
B _isDraggingInputView;
Q _currentSection;
B _inputDelegateCanSupportAnimoji;
B _hasShownAnimojiFirstTimeExperience;
B _shouldRetryFetchingAnimojiRecents;
B _useWideAnimojiCell;
B _hasShownAnimojiCell;
d _frameInset;
B _showingVariants;
q _selectedVariant;
q _currentVariantRow;
@"UIKBTree" _selectedPopupKey;
B _isSearching;
@"UIKeyboardEmojiCategory" _category;
@? _completionBlock;
@"UIResponder<UIKBEmojiHitTestResponder>" _hitTestResponder;
@"NSIndexPath" _tappedSkinToneEmoji;
@"TUIEmojiSearchInputViewController" _emojiSearchInputViewController;
@"TUIEmojiSearchTextField" _emojiSearchField;
@"NSIndexPath" _selectedIndexPath;
@"NSArray" _searchResults;
```

## Properties

```
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"NSIndexPath",&,N,V_selectedIndexPath) selectedIndexPath;
@property (TB,V_isSearching) isSearching;
@property (T@"NSArray",&,N,V_searchResults) searchResults;
@property (T@"UIKeyboardEmojiCategory",W,V_category) category;
@property (T@"UIResponder<UIKBEmojiHitTestResponder>",W,N,V_hitTestResponder) hitTestResponder;
@property (TB,R,V_isDraggingInputView) isDraggingInputView;
@property (T@"NSIndexPath",W,N,V_tappedSkinToneEmoji) tappedSkinToneEmoji;
@property (T@"TUIEmojiSearchInputViewController",&,N,V_emojiSearchInputViewController) emojiSearchInputViewController;
@property (T@"TUIEmojiSearchTextField",&,N,V_emojiSearchField) emojiSearchField;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardEmojiCollectionInputView shouldHighlightEmoji:];
+[UIKeyboardEmojiCollectionInputView wantsScreenTraits];
```

## Instance methods

```
-[UIKeyboardEmojiCollectionInputView handleKeyEvent:];
-[UIKeyboardEmojiCollectionInputView setSearchResults:];
-[UIKeyboardEmojiCollectionInputView setContentScaleFactor:];
-[UIKeyboardEmojiCollectionInputView collectionView:layout:insetForSectionAtIndex:];
-[UIKeyboardEmojiCollectionInputView searchResults];
-[UIKeyboardEmojiCollectionInputView emojiSearchTextFieldDidBecomeInactive:];
-[UIKeyboardEmojiCollectionInputView didMoveToWindow];
-[UIKeyboardEmojiCollectionInputView dimKeys:];
-[UIKeyboardEmojiCollectionInputView emojiSearchTextFieldDidBecomeActive:];
-[UIKeyboardEmojiCollectionInputView setCategory:];
-[UIKeyboardEmojiCollectionInputView initWithFrame:keyplane:key:];
-[UIKeyboardEmojiCollectionInputView emojiSearchTextFieldWillBecomeInactive:];
-[UIKeyboardEmojiCollectionInputView setCompletionBlock:];
-[UIKeyboardEmojiCollectionInputView completionBlock];
-[UIKeyboardEmojiCollectionInputView emojiSearchTextFieldWillBecomeActive:];
-[UIKeyboardEmojiCollectionInputView collectionView:numberOfItemsInSection:];
-[UIKeyboardEmojiCollectionInputView collectionView:willDisplayCell:forItemAtIndexPath:];
-[UIKeyboardEmojiCollectionInputView category];
-[UIKeyboardEmojiCollectionInputView collectionView:cellForItemAtIndexPath:];
-[UIKeyboardEmojiCollectionInputView numberOfSectionsInCollectionView:];
-[UIKeyboardEmojiCollectionInputView collectionView:layout:minimumInteritemSpacingForSectionAtIndex:];
-[UIKeyboardEmojiCollectionInputView dealloc];
-[UIKeyboardEmojiCollectionInputView collectionView:layout:referenceSizeForHeaderInSection:];
-[UIKeyboardEmojiCollectionInputView emojiSearchTextFieldWillClear:];
-[UIKeyboardEmojiCollectionInputView collectionView:layout:sizeForItemAtIndexPath:];
-[UIKeyboardEmojiCollectionInputView scrollViewWillEndDragging:withVelocity:targetContentOffset:];
-[UIKeyboardEmojiCollectionInputView scrollViewWillBeginDragging:];
-[UIKeyboardEmojiCollectionInputView isSearching];
-[UIKeyboardEmojiCollectionInputView collectionView:viewForSupplementaryElementOfKind:atIndexPath:];
-[UIKeyboardEmojiCollectionInputView scrollViewDidEndDecelerating:];
-[UIKeyboardEmojiCollectionInputView collectionView:layout:minimumLineSpacingForSectionAtIndex:];
-[UIKeyboardEmojiCollectionInputView scrollViewDidScroll:];
-[UIKeyboardEmojiCollectionInputView setIsSearching:];
-[UIKeyboardEmojiCollectionInputView updateLastSeenItemForIndexPath:];
-[UIKeyboardEmojiCollectionInputView subTreeHitTest:];
-[UIKeyboardEmojiCollectionInputView _handleBaseKeySelectionEvent:];
-[UIKeyboardEmojiCollectionInputView _handleInitialSelectionEvent:];
-[UIKeyboardEmojiCollectionInputView _handleVariantSelectionEvent:];
-[UIKeyboardEmojiCollectionInputView _recentlyUsedMediaRoundedOffset:recentlyUsedMediaCellWidth:];
-[UIKeyboardEmojiCollectionInputView _setUserHasSelectedSkinToneEmoji:];
-[UIKeyboardEmojiCollectionInputView _shouldShowRecentlyUsedMedia];
-[UIKeyboardEmojiCollectionInputView _userHasSelectedSkinToneEmoji];
-[UIKeyboardEmojiCollectionInputView baseStringIsCoupleEmoji:];
-[UIKeyboardEmojiCollectionInputView cellShouldScrollWhenSelectedAtIndexPath:];
-[UIKeyboardEmojiCollectionInputView didDismissCardForKeyboardMediaController:];
-[UIKeyboardEmojiCollectionInputView didInputSubTree:];
-[UIKeyboardEmojiCollectionInputView didInsertMediaForKeyboardMediaController:];
-[UIKeyboardEmojiCollectionInputView didPresentCardForKeyboardMediaController:];
-[UIKeyboardEmojiCollectionInputView didTearDownRecentsViewForKeyboardMediaController:];
-[UIKeyboardEmojiCollectionInputView distanceInScrollingDirection:];
-[UIKeyboardEmojiCollectionInputView emojiBaseFirstCharacterString:];
-[UIKeyboardEmojiCollectionInputView emojiBaseString:];
-[UIKeyboardEmojiCollectionInputView emojiCategoryTypeForSection:];
-[UIKeyboardEmojiCollectionInputView emojiSearchDidReceiveResults:forExactQuery:autocorrectedQuery:];
-[UIKeyboardEmojiCollectionInputView emojiSearchField];
-[UIKeyboardEmojiCollectionInputView emojiSearchInputViewController];
-[UIKeyboardEmojiCollectionInputView emojiSearchTextFieldDidReset:];
-[UIKeyboardEmojiCollectionInputView firstFullyVisibleHeader];
-[UIKeyboardEmojiCollectionInputView genderEmojiBaseStringNeedVariantSelector:];
-[UIKeyboardEmojiCollectionInputView handleKeyInputForCollectionViewNavigation:];
-[UIKeyboardEmojiCollectionInputView handleKeyInputForFamilySelector:];
-[UIKeyboardEmojiCollectionInputView handleKeyInputForVariantSelector:];
-[UIKeyboardEmojiCollectionInputView handleSelectionEvent:];
-[UIKeyboardEmojiCollectionInputView hitTestResponder];
-[UIKeyboardEmojiCollectionInputView indexForPrettyCategoryDisplay:];
-[UIKeyboardEmojiCollectionInputView initWithFrame:keyplane:key:screenTraits:];
-[UIKeyboardEmojiCollectionInputView insertSelectedEmoji:shouldDismissPopover:];
-[UIKeyboardEmojiCollectionInputView isDraggingInputView];
-[UIKeyboardEmojiCollectionInputView itemInRect:];
-[UIKeyboardEmojiCollectionInputView keyCodeForCurrentEnvironmentFromKeyCode:];
-[UIKeyboardEmojiCollectionInputView keySupportsVariants:];
-[UIKeyboardEmojiCollectionInputView pointInScrollingDirection:];
-[UIKeyboardEmojiCollectionInputView resetSelectionIfNeeded];
-[UIKeyboardEmojiCollectionInputView scrollingEndPoint];
-[UIKeyboardEmojiCollectionInputView scrollingStartPoint];
-[UIKeyboardEmojiCollectionInputView selectedChildSkinToneEmoji:];
-[UIKeyboardEmojiCollectionInputView selectedIndexPath];
-[UIKeyboardEmojiCollectionInputView setEmojiSearchField:];
-[UIKeyboardEmojiCollectionInputView setEmojiSearchInputViewController:];
-[UIKeyboardEmojiCollectionInputView setHitTestResponder:];
-[UIKeyboardEmojiCollectionInputView setSelectedIndexPath:];
-[UIKeyboardEmojiCollectionInputView setTappedSkinToneEmoji:];
-[UIKeyboardEmojiCollectionInputView shouldDismissModalDisplayView:];
-[UIKeyboardEmojiCollectionInputView showingRecents];
-[UIKeyboardEmojiCollectionInputView skinToneWasUsedForEmoji:];
-[UIKeyboardEmojiCollectionInputView snappedXOffsetForOffset:scrubbing:];
-[UIKeyboardEmojiCollectionInputView tappedSkinToneEmoji];
-[UIKeyboardEmojiCollectionInputView treeForCell:];
-[UIKeyboardEmojiCollectionInputView updateHighlightForIndexPath:scrollIfNeeded:animateScroll:];
-[UIKeyboardEmojiCollectionInputView updateOffsetForSearchResults];
-[UIKeyboardEmojiCollectionInputView updatePreferencesForSelectedEmoji:];
-[UIKeyboardEmojiCollectionInputView updateToCategory:];
-[UIKeyboardEmojiCollectionInputView updateToCategoryWithOffsetPercentage:];
-[UIKeyboardEmojiCollectionInputView willDisplayModalActionView:withSubTreeKeyView:completion:];
```
