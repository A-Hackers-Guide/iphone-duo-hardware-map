# `UIWebBrowserView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWebDocumentView`
- Protocols: `UIWebTouchEventsGestureRecognizerDelegate`, `UIWebFormAccessoryDelegate`, `_UIWebRotationDelegate`
- 33 instance variables, 25 properties, 171 instance methods, 2 class methods

## Instance variables

```
@"UIWebFormAccessory" _accessory;
@"NSObject<UIFormPeripheral>" _input;
@"DOMNode" _currentAssistedNode;
@"DOMNode" _assistedNodeStartingFocusRedirects;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputViewBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _addressViewBounds;
d _lastAdjustmentForScroller;
Q _audioSessionCategoryOverride;
b1 _accessoryEnabled;
b1 _forceInputView;
b1 _formIsAutoFilling;
b1 _inputViewObeysDOMFocus;
b1 _allowDOMFocusRedirects;
b1 _hasEditedTextField;
b1 _alwaysDispatchesScrollEvents;
b1 _allowsPictureInPictureVideo;
b1 _allowsLinkPreview;
@"UIWebTouchEventsGestureRecognizer" _webTouchEventsGestureRecognizer;
@"UIWebFormDelegate" _formDelegate;
@"UIResponder" _editingDelegateForEverythingExceptForms;
Q _dispatchedTouchEvents;
@"NSMutableArray" _deferredTouchEvents;
@"NSHashTable" _activeHighlighters;
@"NSMutableSet" _overflowScrollViewsPendingInsertion;
@"NSMutableSet" _overflowScrollViewsPendingDeletion;
@"NSMutableSet" _overflowScrollViews;
@"NSLock" _pendingOverflowDataLock;
@"NSMutableArray" _pendingOverflowScrolls;
B _pendingGeometryChangeAfterOverflowScroll;
@"NSMutableDictionary" _focusPreservingTokens;
{?="all"@"NSMutableArray""html"@"NSMutableArray""javascript"@"NSMutableArray""css"@"NSMutableArray""error"@"NSMutableArray""warning"@"NSMutableArray""tip"@"NSMutableArray""log"@"NSMutableArray"} _messages;
{?="view"@"UIWebPDFView""timer"@"NSTimer"} _pdf;
@"<UIWebAutoFillDelegate>" _autoFillDelegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIWebFormAccessory",&,N,V_accessory) _accessory;
@property (T@"NSObject<UIFormPeripheral>",&,N,V_input) _input;
@property (T@"DOMNode",&,N,V_currentAssistedNode) _currentAssistedNode;
@property (TB,N,GisAccessoryEnabled,V_accessoryEnabled) accessoryEnabled;
@property (TB,N,V_inputViewObeysDOMFocus) inputViewObeysDOMFocus;
@property (TB,N,V_allowDOMFocusRedirects) allowDOMFocusRedirects;
@property (TB,R,N,V_hasEditedTextField) hasEditedTextField;
@property (T@"UIResponder",N,V_editingDelegateForEverythingExceptForms) _editingDelegateForEverythingExceptForms;
@property (TB,N) allowsInlineMediaPlayback;
@property (TB,N) mediaPlaybackRequiresUserAction;
@property (TB,R,N) isDispatchingTouchEvents;
@property (TB,N) alwaysDispatchesScrollEvents;
@property (T@"<UIWebAutoFillDelegate>",N,V_autoFillDelegate) autoFillDelegate;
@property (TI,N) audioSessionCategoryOverride;
@property (T@"NSString",N) networkInterfaceName;
@property (TB,N) allowsPictureInPictureVideo;
@property (TB,N) allowsLinkPreview;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIWebBrowserView initialize];
+[UIWebBrowserView getUIWebBrowserViewForWebFrame:];
```

## Instance methods

```
-[UIWebBrowserView isEditable];
-[UIWebBrowserView _keyboardWillShow:];
-[UIWebBrowserView isAutoFillMode];
-[UIWebBrowserView inputAccessoryView];
-[UIWebBrowserView _keyboardWillChangeFrame:];
-[UIWebBrowserView _keyboardDidHide:];
-[UIWebBrowserView _keyboardWillHide:];
-[UIWebBrowserView _transliterateChinese:];
-[UIWebBrowserView dealloc];
-[UIWebBrowserView isDispatchingTouchEvents];
-[UIWebBrowserView _promptForReplace:];
-[UIWebBrowserView keyCommands];
-[UIWebBrowserView _didMoveFromWindow:toWindow:];
-[UIWebBrowserView resignFirstResponder];
-[UIWebBrowserView setBounds:];
-[UIWebBrowserView inputView];
-[UIWebBrowserView copy:];
-[UIWebBrowserView setFrame:];
-[UIWebBrowserView _keyboardDidChangeFrame:];
-[UIWebBrowserView _input];
-[UIWebBrowserView initWithFrame:];
-[UIWebBrowserView canPerformAction:withSender:];
-[UIWebBrowserView _autoFillFrame:];
-[UIWebBrowserView mediaPlaybackRequiresUserAction];
-[UIWebBrowserView textFormElement];
-[UIWebBrowserView _deferWebEvent:];
-[UIWebBrowserView assistFormNode:];
-[UIWebBrowserView setAllowsPictureInPictureVideo:];
-[UIWebBrowserView _absoluteUrlRelativeToDocumentURL:];
-[UIWebBrowserView _accessory];
-[UIWebBrowserView _activeRectForRectToCenter:];
-[UIWebBrowserView _addAdditionalSubview:];
-[UIWebBrowserView _assistFormNode:];
-[UIWebBrowserView _beginAllowingFocusRedirects];
-[UIWebBrowserView _centerRect:forSizeChange:withVisibleHeight:pinningEdge:];
-[UIWebBrowserView _centerRect:forSizeChange:withVisibleHeight:pinningEdge:toValue:];
-[UIWebBrowserView _clearAllConsoleMessages];
-[UIWebBrowserView _clearFormAutoFillStateForFrame:];
-[UIWebBrowserView _clearSelectionAndUI];
-[UIWebBrowserView _clearToken:];
-[UIWebBrowserView _collectAdditionalSubviews];
-[UIWebBrowserView _convertWindowPointToViewport:];
-[UIWebBrowserView _currentAssistedNode];
-[UIWebBrowserView _defaultScrollViewContentSize];
-[UIWebBrowserView _didScroll];
-[UIWebBrowserView _dispatchWebEvent:];
-[UIWebBrowserView _displayFormNodeInputView];
-[UIWebBrowserView _dumpWebArchiveAtPath:];
-[UIWebBrowserView _editingDelegate];
-[UIWebBrowserView _editingDelegateForEverythingExceptForms];
-[UIWebBrowserView _endAllowingFocusRedirects];
-[UIWebBrowserView _endDeferringEvents];
-[UIWebBrowserView _focusAndAssistFormNode:];
-[UIWebBrowserView _handleDeferredEvents];
-[UIWebBrowserView _hasSubviewContainingWebContent:];
-[UIWebBrowserView _isAutoFilling];
-[UIWebBrowserView _keepKeyboardVisibleDuringFocusRedirects];
-[UIWebBrowserView _keyboardResponder];
-[UIWebBrowserView _nextAccessoryTab:];
-[UIWebBrowserView _noteOverflowScrollViewPendingDeletion:];
-[UIWebBrowserView _noteOverflowScrollViewPendingInsertion:];
-[UIWebBrowserView _overflowScrollView:didEndScrollingForNode:];
-[UIWebBrowserView _overflowScrollView:scrollOffsetChangedForNode:whileScrolling:];
-[UIWebBrowserView _overflowScrollView:willStartScrollingForNode:];
-[UIWebBrowserView _preserveFocusWithToken:destructively:];
-[UIWebBrowserView _prevAccessoryTab:];
-[UIWebBrowserView _reloadInputViewsAfterPotentialFocusRedirect];
-[UIWebBrowserView _removeAdditionalSubview:];
-[UIWebBrowserView _removeFindOnPageHighlighter:];
-[UIWebBrowserView _requiresKeyboardResetOnReload];
-[UIWebBrowserView _requiresKeyboardWhenFirstResponder];
-[UIWebBrowserView _resetFormDataForFrame:];
-[UIWebBrowserView _resignFirstResponderAndBlurFocusedElement];
-[UIWebBrowserView _restoreFocusWithToken:];
-[UIWebBrowserView _scrollCaretToVisible:];
-[UIWebBrowserView _setInputViewBoundsForAutomaticKeyboardInfo:adjustScrollView:];
-[UIWebBrowserView _setSelectedDOMRangeAndUpdateUI:];
-[UIWebBrowserView _setUnobscuredSafeAreaInsets:];
-[UIWebBrowserView _shouldDeferEvents];
-[UIWebBrowserView _shouldRestorationInputViewsOnlyWhenKeepingFirstResponder];
-[UIWebBrowserView _startAssistingKeyboard];
-[UIWebBrowserView _startAssistingNode:];
-[UIWebBrowserView _startDeferringEvents];
-[UIWebBrowserView _startRelinquishingFirstResponderToFocusedElement];
-[UIWebBrowserView _startURLificationIfNeededCoalesce:];
-[UIWebBrowserView _stopAssistingFormNode];
-[UIWebBrowserView _stopAssistingKeyboard];
-[UIWebBrowserView _stopAssistingNode:];
-[UIWebBrowserView _stopRelinquishingFirstResponderToFocusedElement];
-[UIWebBrowserView _updateAccessory];
-[UIWebBrowserView _updateAutoFillButton];
-[UIWebBrowserView _updateFixedPositionContent];
-[UIWebBrowserView _updateFixedPositioningObjectsLayoutAfterScroll];
-[UIWebBrowserView _updateFixedPositioningObjectsLayoutAfterVisibleGeometryChange];
-[UIWebBrowserView _updateFixedPositioningObjectsLayoutDuringScroll];
-[UIWebBrowserView _updateFixedPositioningObjectsLayoutSoon];
-[UIWebBrowserView _updateScrollerViewForInputView:];
-[UIWebBrowserView _webThreadOverflowScrollOffsetChanged];
-[UIWebBrowserView _webTouchEventsRecognized:];
-[UIWebBrowserView _webViewFormEditedStatusHasChanged:];
-[UIWebBrowserView _zoomToNode:forceScroll:];
-[UIWebBrowserView _zoomToRect:ensuringVisibilityOfRect:withScale:forceScroll:];
-[UIWebBrowserView _zoomToRect:ensuringVisibilityOfRect:withScale:forceScroll:formAssistantFrame:animationDuration:];
-[UIWebBrowserView _zoomToRect:withScale:];
-[UIWebBrowserView acceptedAutoFillWord:];
-[UIWebBrowserView accessoryAutoFill];
-[UIWebBrowserView accessoryClear];
-[UIWebBrowserView accessoryDone];
-[UIWebBrowserView accessoryTab:];
-[UIWebBrowserView activeRectForRectOfInterest:];
-[UIWebBrowserView addFindOnPageHighlighter];
-[UIWebBrowserView allowDOMFocusRedirects];
-[UIWebBrowserView allowsInlineMediaPlayback];
-[UIWebBrowserView allowsLinkPreview];
-[UIWebBrowserView allowsPictureInPictureVideo];
-[UIWebBrowserView alwaysDispatchesScrollEvents];
-[UIWebBrowserView appendOverflowScrollForNode:offset:whileScrolling:];
-[UIWebBrowserView audioSessionCategoryOverride];
-[UIWebBrowserView autoFillDelegate];
-[UIWebBrowserView clearMessagesMatchingMask:];
-[UIWebBrowserView considerHeightOfRectOfInterestForRotation];
-[UIWebBrowserView contentSizeForScrollView:];
-[UIWebBrowserView formDelegateTextDidChange];
-[UIWebBrowserView formElement];
-[UIWebBrowserView hasEditedTextField];
-[UIWebBrowserView heightToKeepVisible];
-[UIWebBrowserView initWithWebView:frame:];
-[UIWebBrowserView inputViewObeysDOMFocus];
-[UIWebBrowserView installGestureRecognizers];
-[UIWebBrowserView isAccessoryEnabled];
-[UIWebBrowserView isAnyTouchOverActiveArea:];
-[UIWebBrowserView messagesMatchingMask:];
-[UIWebBrowserView minimumVerticalContentOffset];
-[UIWebBrowserView networkInterfaceName];
-[UIWebBrowserView playsNicelyWithGestures];
-[UIWebBrowserView rectOfInterestForRotation];
-[UIWebBrowserView redrawScaledDocument];
-[UIWebBrowserView rotateEnclosingScrollViewToFrame:];
-[UIWebBrowserView scaleForProposedNewScale:andOldScale:];
-[UIWebBrowserView scalesForContainerSize:];
-[UIWebBrowserView setAccessoryEnabled:];
-[UIWebBrowserView setAllowDOMFocusRedirects:];
-[UIWebBrowserView setAllowsInlineMediaPlayback:];
-[UIWebBrowserView setAllowsLinkPreview:];
-[UIWebBrowserView setAlwaysDispatchesScrollEvents:];
-[UIWebBrowserView setAudioSessionCategoryOverride:];
-[UIWebBrowserView setAutoFillDelegate:];
-[UIWebBrowserView setInputViewObeysDOMFocus:];
-[UIWebBrowserView setMediaPlaybackRequiresUserAction:];
-[UIWebBrowserView setNetworkInterfaceName:];
-[UIWebBrowserView set_accessory:];
-[UIWebBrowserView set_currentAssistedNode:];
-[UIWebBrowserView set_editingDelegateForEverythingExceptForms:];
-[UIWebBrowserView set_input:];
-[UIWebBrowserView shouldIgnoreWebTouch];
-[UIWebBrowserView simulateDidScroll];
-[UIWebBrowserView textDocument];
-[UIWebBrowserView updateBoundariesOfScrollView:withScales:];
-[UIWebBrowserView webView:addMessageToConsole:withSource:];
-[UIWebBrowserView webView:didCreateOrUpdateScrollingLayer:withContentsLayer:scrollSize:forNode:allowHorizontalScrollbar:allowVerticalScrollbar:];
-[UIWebBrowserView webView:didFailLoadWithError:forFrame:];
-[UIWebBrowserView webView:didFinishLoadForFrame:];
-[UIWebBrowserView webView:didFirstLayoutInFrame:];
-[UIWebBrowserView webView:didFirstVisuallyNonEmptyLayoutInFrame:];
-[UIWebBrowserView webView:didStartProvisionalLoadForFrame:];
-[UIWebBrowserView webView:elementDidBlurNode:];
-[UIWebBrowserView webView:elementDidFocusNode:];
-[UIWebBrowserView webView:willCloseFrame:];
-[UIWebBrowserView webView:willRemoveScrollingLayer:withContentsLayer:forNode:];
-[UIWebBrowserView webViewDidCommitCompositingLayerChanges:];
-[UIWebBrowserView webViewDidPreventDefaultForEvent:];
```
