# `UIKeyboardEmojiAndStickerCollectionInputView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardEmojiKeyView`
- Protocols: `UIKeyboardMediaControllerDelegate`, `UIKeyboardEmojiAndStickerCollectionViewCellDelegate`, `UIKeyboardEmojiAndStickerCollectionViewDelegate`, `UIGestureRecognizerDelegate`, `UICollectionViewDataSource`, `UICollectionViewDelegate`, `TUIEmojiSearchInputViewControllerDelegate`
- 38 instance variables, 19 properties, 172 instance methods, 2 class methods

## Instance variables

```
@"UIKeyboardEmojiAndStickerCollectionView" _collectionView;
@"UICollectionViewFlowLayout" _flowLayout;
@"UIKeyboardEmojiGraphicsTraits" _emojiGraphicsTraits;
B _isDraggingInputView;
Q _currentSection;
@"NSIndexPath" _currentIndexPath;
B _inputDelegateCanSupportAnimoji;
B _hasShownAnimojiFirstTimeExperience;
B _shouldRetryFetchingAnimojiRecents;
B _useWideAnimojiCell;
B _hasShownAnimojiCell;
B _hasCompletedInitialDisplay;
B _isRearranging;
{CGPoint="x"d"y"d} _touchOffsetForMovingCell;
d _frameInset;
B _showingVariants;
q _selectedVariant;
q _currentVariantRow;
@"NSHashTable" _delegates;
@"UIKBTree" _selectedPopupKey;
@"UILongPressGestureRecognizer" _longPressRecognizer;
@"UITapGestureRecognizer" _tapRecognizer;
@"NSObject<OS_os_log>" _logger;
@"UIKeyboardEmojiAndStickerCollectionInputViewKeylineView" _keylineView;
B _isSearching;
B _didAcceptRestrictedDistributionTerms;
@"UIKeyboardEmojiCategory" _category;
@? _completionBlock;
@"UIResponder<UIKBEmojiHitTestResponder>" _hitTestResponder;
@"NSIndexPath" _tappedSkinToneEmoji;
@"NSArray" _searchResults;
@"TUIEmojiSearchInputViewController" _emojiSearchInputViewController;
@"TUIEmojiSearchTextField" _emojiSearchField;
@"NSString" _bundleId;
@"NSIndexPath" _selectedIndexPath;
@"NSIndexPath" _unavailableLaunchPath;
@"STKImageGlyphDataSource" _imageGlyphDataSource;
@"UICollectionViewDiffableDataSource" _dataSource;
```

## Properties

```
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"NSIndexPath",&,N,V_selectedIndexPath) selectedIndexPath;
@property (T@"NSIndexPath",&,N,V_unavailableLaunchPath) unavailableLaunchPath;
@property (TB,N,V_isSearching) isSearching;
@property (T@"STKImageGlyphDataSource",&,N,V_imageGlyphDataSource) imageGlyphDataSource;
@property (T@"UICollectionViewDiffableDataSource",&,N,V_dataSource) dataSource;
@property (TB,N,V_didAcceptRestrictedDistributionTerms) didAcceptRestrictedDistributionTerms;
@property (T@"UIKeyboardEmojiCategory",W,V_category) category;
@property (T@"UIResponder<UIKBEmojiHitTestResponder>",W,N,V_hitTestResponder) hitTestResponder;
@property (TB,R,V_isDraggingInputView) isDraggingInputView;
@property (T@"NSIndexPath",W,N,V_tappedSkinToneEmoji) tappedSkinToneEmoji;
@property (T@"NSArray",&,N,V_searchResults) searchResults;
@property (T@"TUIEmojiSearchInputViewController",&,N,V_emojiSearchInputViewController) emojiSearchInputViewController;
@property (T@"TUIEmojiSearchTextField",&,N,V_emojiSearchField) emojiSearchField;
@property (T@"NSString",C,N,V_bundleId) bundleId;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardEmojiAndStickerCollectionInputView shouldHighlightEmoji:];
+[UIKeyboardEmojiAndStickerCollectionInputView wantsScreenTraits];
```

## Instance methods

```
-[UIKeyboardEmojiAndStickerCollectionInputView handleKeyEvent:];
-[UIKeyboardEmojiAndStickerCollectionInputView setSearchResults:];
-[UIKeyboardEmojiAndStickerCollectionInputView setContentScaleFactor:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:layout:insetForSectionAtIndex:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:didEndDisplayingCell:forItemAtIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView searchResults];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchTextFieldDidBecomeInactive:];
-[UIKeyboardEmojiAndStickerCollectionInputView didMoveToWindow];
-[UIKeyboardEmojiAndStickerCollectionInputView dimKeys:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchTextFieldDidBecomeActive:];
-[UIKeyboardEmojiAndStickerCollectionInputView setCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView initWithFrame:keyplane:key:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchTextFieldWillBecomeInactive:];
-[UIKeyboardEmojiAndStickerCollectionInputView setCompletionBlock:];
-[UIKeyboardEmojiAndStickerCollectionInputView completionBlock];
-[UIKeyboardEmojiAndStickerCollectionInputView displayLayer:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchTextFieldWillBecomeActive:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:numberOfItemsInSection:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:willDisplayCell:forItemAtIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView _handleLongPress:];
-[UIKeyboardEmojiAndStickerCollectionInputView topPadding];
-[UIKeyboardEmojiAndStickerCollectionInputView _handleTap:];
-[UIKeyboardEmojiAndStickerCollectionInputView category];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:cellForItemAtIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView numberOfSectionsInCollectionView:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:layout:minimumInteritemSpacingForSectionAtIndex:];
-[UIKeyboardEmojiAndStickerCollectionInputView dealloc];
-[UIKeyboardEmojiAndStickerCollectionInputView targetRectForSectionIndex:];
-[UIKeyboardEmojiAndStickerCollectionInputView setBundleId:];
-[UIKeyboardEmojiAndStickerCollectionInputView setDataSource:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:layout:referenceSizeForHeaderInSection:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchTextFieldWillClear:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:layout:sizeForItemAtIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView scrollViewWillEndDragging:withVelocity:targetContentOffset:];
-[UIKeyboardEmojiAndStickerCollectionInputView accessibilityIdentifier];
-[UIKeyboardEmojiAndStickerCollectionInputView configureDataSource];
-[UIKeyboardEmojiAndStickerCollectionInputView dataSource];
-[UIKeyboardEmojiAndStickerCollectionInputView bundleId];
-[UIKeyboardEmojiAndStickerCollectionInputView _addDelegate:];
-[UIKeyboardEmojiAndStickerCollectionInputView scrollViewWillBeginDragging:];
-[UIKeyboardEmojiAndStickerCollectionInputView isSearching];
-[UIKeyboardEmojiAndStickerCollectionInputView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:viewForSupplementaryElementOfKind:atIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView currentlyFocusedSectionIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView scrollViewDidEndDecelerating:];
-[UIKeyboardEmojiAndStickerCollectionInputView collectionView:layout:minimumLineSpacingForSectionAtIndex:];
-[UIKeyboardEmojiAndStickerCollectionInputView currentlyFocusedIndexPath];
-[UIKeyboardEmojiAndStickerCollectionInputView scrollViewDidScroll:];
-[UIKeyboardEmojiAndStickerCollectionInputView setIsSearching:];
-[UIKeyboardEmojiAndStickerCollectionInputView updateLastSeenItemForIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView subTreeHitTest:];
-[UIKeyboardEmojiAndStickerCollectionInputView _handleBaseKeySelectionEvent:];
-[UIKeyboardEmojiAndStickerCollectionInputView _handleInitialSelectionEvent:];
-[UIKeyboardEmojiAndStickerCollectionInputView _handleVariantSelectionEvent:];
-[UIKeyboardEmojiAndStickerCollectionInputView _notifyDelegatesRearrangeModeChanged:];
-[UIKeyboardEmojiAndStickerCollectionInputView _removeDelegate:];
-[UIKeyboardEmojiAndStickerCollectionInputView _setRearrangeMode:];
-[UIKeyboardEmojiAndStickerCollectionInputView _setUserHasSelectedSkinToneEmoji:];
-[UIKeyboardEmojiAndStickerCollectionInputView _setupLongPressGestureRecognizer];
-[UIKeyboardEmojiAndStickerCollectionInputView _setupTapGestureRecognizer];
-[UIKeyboardEmojiAndStickerCollectionInputView _shouldShowRecentlyUsedMedia];
-[UIKeyboardEmojiAndStickerCollectionInputView _updateRearrangeModeForCell:atIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView _usageSourceFromSection:];
-[UIKeyboardEmojiAndStickerCollectionInputView _userHasSelectedSkinToneEmoji];
-[UIKeyboardEmojiAndStickerCollectionInputView baseStringIsCoupleEmoji:];
-[UIKeyboardEmojiAndStickerCollectionInputView categoryHeaderFontSize];
-[UIKeyboardEmojiAndStickerCollectionInputView categoryHeaderHeight];
-[UIKeyboardEmojiAndStickerCollectionInputView cellRectToRevealFullCell:];
-[UIKeyboardEmojiAndStickerCollectionInputView cellShouldScrollWhenSelectedAtIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView datasourceIsReady];
-[UIKeyboardEmojiAndStickerCollectionInputView deleteImageGlyph:atPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView didAcceptOnboarding];
-[UIKeyboardEmojiAndStickerCollectionInputView didAcceptRestrictedDistributionTerms];
-[UIKeyboardEmojiAndStickerCollectionInputView didDismissCardForKeyboardMediaController:];
-[UIKeyboardEmojiAndStickerCollectionInputView didDismissOnboarding];
-[UIKeyboardEmojiAndStickerCollectionInputView didInputSubTree:];
-[UIKeyboardEmojiAndStickerCollectionInputView didInsertMediaForKeyboardMediaController:];
-[UIKeyboardEmojiAndStickerCollectionInputView didPresentCardForKeyboardMediaController:];
-[UIKeyboardEmojiAndStickerCollectionInputView didTearDownRecentsViewForKeyboardMediaController:];
-[UIKeyboardEmojiAndStickerCollectionInputView didUpdateImageGlyphPermissions];
-[UIKeyboardEmojiAndStickerCollectionInputView distanceInScrollingDirection:];
-[UIKeyboardEmojiAndStickerCollectionInputView doesShowMemoji];
-[UIKeyboardEmojiAndStickerCollectionInputView doesShowStickers];
-[UIKeyboardEmojiAndStickerCollectionInputView doesSupportImageGlyph];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiBaseFirstCharacterString:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiBaseString:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiCategoryIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiCategoryTypeForSection:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiKeyWidth];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchDidReceiveResults:forExactQuery:autocorrectedQuery:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchField];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchInputViewController];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSearchTextFieldDidReset:];
-[UIKeyboardEmojiAndStickerCollectionInputView emojiSectionIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView genderEmojiBaseStringNeedVariantSelector:];
-[UIKeyboardEmojiAndStickerCollectionInputView handleKeyInputForCollectionViewNavigation:];
-[UIKeyboardEmojiAndStickerCollectionInputView handleKeyInputForFamilySelector:];
-[UIKeyboardEmojiAndStickerCollectionInputView handleKeyInputForVariantSelector:];
-[UIKeyboardEmojiAndStickerCollectionInputView handleScrollViewDynamicPagination:];
-[UIKeyboardEmojiAndStickerCollectionInputView handleSelectionEvent:];
-[UIKeyboardEmojiAndStickerCollectionInputView hasVerticalScrolling];
-[UIKeyboardEmojiAndStickerCollectionInputView hitTestResponder];
-[UIKeyboardEmojiAndStickerCollectionInputView imageGlyphDataSource];
-[UIKeyboardEmojiAndStickerCollectionInputView indexForPrettyCategoryDisplay:];
-[UIKeyboardEmojiAndStickerCollectionInputView initWithFrame:keyplane:key:screenTraits:];
-[UIKeyboardEmojiAndStickerCollectionInputView insertImageGlyph:dismiss:];
-[UIKeyboardEmojiAndStickerCollectionInputView insertSelectedEmoji:shouldDismissPopover:];
-[UIKeyboardEmojiAndStickerCollectionInputView isCellMostlyOffscreen:];
-[UIKeyboardEmojiAndStickerCollectionInputView isDraggingInputView];
-[UIKeyboardEmojiAndStickerCollectionInputView isEmojiCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView isGenmojiCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView isMemojiCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView isRearrangeableCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView isRearrangingAllowed];
-[UIKeyboardEmojiAndStickerCollectionInputView isRecentCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView isSearchCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView isStickersCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView itemInRect:];
-[UIKeyboardEmojiAndStickerCollectionInputView keyCodeForCurrentEnvironmentFromKeyCode:];
-[UIKeyboardEmojiAndStickerCollectionInputView keySupportsVariants:];
-[UIKeyboardEmojiAndStickerCollectionInputView memojiCategoryIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView memojiSectionIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView numberOfPrefixCategories];
-[UIKeyboardEmojiAndStickerCollectionInputView numberOfPrefixSections];
-[UIKeyboardEmojiAndStickerCollectionInputView pointInScrollingDirection:];
-[UIKeyboardEmojiAndStickerCollectionInputView rearrangeStateChanged:];
-[UIKeyboardEmojiAndStickerCollectionInputView recentCategoryIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView recentSectionIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView recentsIndexPath];
-[UIKeyboardEmojiAndStickerCollectionInputView resetSelectionIfNeeded];
-[UIKeyboardEmojiAndStickerCollectionInputView rowsInSection:];
-[UIKeyboardEmojiAndStickerCollectionInputView scrollingEndPoint];
-[UIKeyboardEmojiAndStickerCollectionInputView scrollingStartPoint];
-[UIKeyboardEmojiAndStickerCollectionInputView sectionForCategoryType:];
-[UIKeyboardEmojiAndStickerCollectionInputView selectedChildSkinToneEmoji:];
-[UIKeyboardEmojiAndStickerCollectionInputView selectedIndexPath];
-[UIKeyboardEmojiAndStickerCollectionInputView setDidAcceptRestrictedDistributionTerms:];
-[UIKeyboardEmojiAndStickerCollectionInputView setDidShowGenmojiSuggestionsOnboardingAccepting:];
-[UIKeyboardEmojiAndStickerCollectionInputView setEmojiSearchField:];
-[UIKeyboardEmojiAndStickerCollectionInputView setEmojiSearchInputViewController:];
-[UIKeyboardEmojiAndStickerCollectionInputView setHitTestResponder:];
-[UIKeyboardEmojiAndStickerCollectionInputView setImageGlyphDataSource:];
-[UIKeyboardEmojiAndStickerCollectionInputView setSelectedIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView setTappedSkinToneEmoji:];
-[UIKeyboardEmojiAndStickerCollectionInputView setUnavailableLaunchPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView shouldDismissModalDisplayView:];
-[UIKeyboardEmojiAndStickerCollectionInputView showingRecents];
-[UIKeyboardEmojiAndStickerCollectionInputView skinToneWasUsedForEmoji:];
-[UIKeyboardEmojiAndStickerCollectionInputView snappedXOffsetForOffset:scrubbing:];
-[UIKeyboardEmojiAndStickerCollectionInputView stickerCellForIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView stickersCategoryIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView stickersSectionIndex];
-[UIKeyboardEmojiAndStickerCollectionInputView supportsDatasourceIsReady];
-[UIKeyboardEmojiAndStickerCollectionInputView tappedSkinToneEmoji];
-[UIKeyboardEmojiAndStickerCollectionInputView targetRectForIndexPath:atScrollPosition:];
-[UIKeyboardEmojiAndStickerCollectionInputView translatedEmojiCategoryForSection:];
-[UIKeyboardEmojiAndStickerCollectionInputView treeForCell:];
-[UIKeyboardEmojiAndStickerCollectionInputView treeForStickerCell:];
-[UIKeyboardEmojiAndStickerCollectionInputView trulyVisibleIndexPaths];
-[UIKeyboardEmojiAndStickerCollectionInputView unavailableLaunchPath];
-[UIKeyboardEmojiAndStickerCollectionInputView updateDataSourceSnapshot];
-[UIKeyboardEmojiAndStickerCollectionInputView updateDataSourceSnapshotAnimated:];
-[UIKeyboardEmojiAndStickerCollectionInputView updateDataSourceWithSnapshot:animated:];
-[UIKeyboardEmojiAndStickerCollectionInputView updateHighlightForIndexPath:scrollIfNeeded:animateScroll:];
-[UIKeyboardEmojiAndStickerCollectionInputView updateOffsetForSearchResultsAnimated:];
-[UIKeyboardEmojiAndStickerCollectionInputView updatePreferencesForSelectedEmoji:];
-[UIKeyboardEmojiAndStickerCollectionInputView updateToCategory:];
-[UIKeyboardEmojiAndStickerCollectionInputView updateToCategoryWithOffsetPercentage:];
-[UIKeyboardEmojiAndStickerCollectionInputView updateToIndexPath:];
-[UIKeyboardEmojiAndStickerCollectionInputView verticalNeighborForIndexPath:up:byPage:];
-[UIKeyboardEmojiAndStickerCollectionInputView willDisplayModalActionView:withSubTreeKeyView:completion:];
```
