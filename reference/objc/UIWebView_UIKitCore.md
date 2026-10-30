# `UIWebView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `WebPolicyDelegate`, `NSCoding`, `UIScrollViewDelegate`
- 1 instance variables, 25 properties, 175 instance methods, 4 class methods

## Instance variables

```
@"UIWebViewInternal" _internal;
```

## Properties

```
@property (T@"<UIWebViewDelegate>",N) delegate;
@property (T@"UIScrollView",R,N) scrollView;
@property (T@"NSURLRequest",R,N) request;
@property (TB,R,N,GcanGoBack) canGoBack;
@property (TB,R,N,GcanGoForward) canGoForward;
@property (TB,R,N,GisLoading) loading;
@property (TB,N) scalesPageToFit;
@property (TB,N) detectsPhoneNumbers;
@property (TQ,N) dataDetectorTypes;
@property (TB,N) allowsInlineMediaPlayback;
@property (TB,N) mediaPlaybackRequiresUserAction;
@property (TB,N) mediaPlaybackAllowsAirPlay;
@property (TB,N) suppressesIncrementalRendering;
@property (TB,N) keyboardDisplayRequiresUserAction;
@property (Tq,N) paginationMode;
@property (Tq,N) paginationBreakingMode;
@property (Td,N) pageLength;
@property (Td,N) gapBetweenPages;
@property (TQ,R,N) pageCount;
@property (TB,N) allowsPictureInPictureMediaPlayback;
@property (TB,N) allowsLinkPreview;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIWebView initialize];
+[UIWebView _fixPathsForSandboxDirectoryChange];
+[UIWebView _relativePathFromAbsolutePath:removingPathComponents:];
+[UIWebView _updatePersistentStoragePaths];
```

## Instance methods

```
-[UIWebView selectAll:];
-[UIWebView _share:];
-[UIWebView _define:];
-[UIWebView _scrollView];
-[UIWebView decodeRestorableStateWithCoder:];
-[UIWebView goBack];
-[UIWebView _addShortcut:];
-[UIWebView goForward];
-[UIWebView _translate:];
-[UIWebView pageCount];
-[UIWebView encodeRestorableStateWithCoder:];
-[UIWebView _dynamicUserInterfaceTraitDidChange];
-[UIWebView scrollViewDidEndZooming:withView:atScale:];
-[UIWebView viewForZoomingInScrollView:];
-[UIWebView stopLoading];
-[UIWebView canGoForward];
-[UIWebView scrollView];
-[UIWebView scrollViewDidScrollToTop:];
-[UIWebView dealloc];
-[UIWebView setOpaque:];
-[UIWebView scrollViewDidChangeAdjustedContentInset:];
-[UIWebView canGoBack];
-[UIWebView reload];
-[UIWebView scrollViewDidZoom:];
-[UIWebView setBounds:];
-[UIWebView request];
-[UIWebView setBackgroundColor:];
-[UIWebView sizeThatFits:];
-[UIWebView select:];
-[UIWebView setDelegate:];
-[UIWebView copy:];
-[UIWebView scrollViewWillBeginDragging:];
-[UIWebView encodeWithCoder:];
-[UIWebView delegate];
-[UIWebView loadHTMLString:baseURL:];
-[UIWebView _reportError:];
-[UIWebView setFrame:];
-[UIWebView isElementAccessibilityExposedToInterfaceBuilder];
-[UIWebView isLoading];
-[UIWebView scrollViewDidEndDragging:willDecelerate:];
-[UIWebView setDataDetectorTypes:];
-[UIWebView dataDetectorTypes];
-[UIWebView initWithCoder:];
-[UIWebView scrollViewWillBeginZooming:withView:];
-[UIWebView _populateArchivedSubviews:];
-[UIWebView scrollViewDidEndDecelerating:];
-[UIWebView _updateRequest];
-[UIWebView initWithFrame:];
-[UIWebView canPerformAction:withSender:];
-[UIWebView scrollViewDidScroll:];
-[UIWebView _finishRotation];
-[UIWebView _pdfViewHandler];
-[UIWebView _setPageLength:];
-[UIWebView mediaPlaybackRequiresUserAction];
-[UIWebView webView:decidePolicyForMIMEType:request:frame:decisionListener:];
-[UIWebView _paginationMode];
-[UIWebView _updateOpaqueAndBackgroundColor];
-[UIWebView gapBetweenPages];
-[UIWebView scalesPageToFit];
-[UIWebView _allowsPictureInPictureVideo];
-[UIWebView _alwaysConstrainsScale];
-[UIWebView _alwaysDispatchesScrollEvents];
-[UIWebView _appliesExclusiveTouchToSubviewTree];
-[UIWebView _audioSessionCategoryOverride];
-[UIWebView _beginRotation];
-[UIWebView _browserView];
-[UIWebView _didCompleteScrolling];
-[UIWebView _didRotate:];
-[UIWebView _documentView];
-[UIWebView _effectiveAppearanceIsDark];
-[UIWebView _effectiveTraitsUseElevatedUserInterfaceLevel];
-[UIWebView _frameOrBoundsChanged];
-[UIWebView _gapBetweenPages];
-[UIWebView _initWithFrame:enableReachability:];
-[UIWebView _initWithWebView:];
-[UIWebView _networkInterfaceName];
-[UIWebView _pageCount];
-[UIWebView _pageLength];
-[UIWebView _paginationBehavesLikeColumns];
-[UIWebView _rescaleDocument];
-[UIWebView _setAllowsPictureInPictureVideo:];
-[UIWebView _setAlwaysConstrainsScale:];
-[UIWebView _setAlwaysDispatchesScrollEvents:];
-[UIWebView _setAudioSessionCategoryOverride:];
-[UIWebView _setDrawInWebThread:];
-[UIWebView _setDrawsCheckeredPattern:];
-[UIWebView _setGapBetweenPages:];
-[UIWebView _setNetworkInterfaceName:];
-[UIWebView _setOverridesOrientationChangeEventHandling:];
-[UIWebView _setPaginationBehavesLikeColumns:];
-[UIWebView _setPaginationMode:];
-[UIWebView _setRichTextReaderViewportSettings];
-[UIWebView _setScalesPageToFitViewportSettings];
-[UIWebView _setSelectionEnabled:];
-[UIWebView _setWebSelectionEnabled:];
-[UIWebView _shouldUseViewForSceneDraggingBehavior];
-[UIWebView _updateBrowserViewExposedScrollViewRect];
-[UIWebView _updateCheckeredPattern];
-[UIWebView _updateScrollViewInsetAdjustmentBehavior];
-[UIWebView _updateScrollerViewForInputView:];
-[UIWebView _updateViewSettings];
-[UIWebView _webView:commitPreview:];
-[UIWebView _webView:didChangeAvoidsUnsafeArea:];
-[UIWebView _webView:didDismissPreview:committing:];
-[UIWebView _webView:presentationRectsForPreview:];
-[UIWebView _webView:presentationSnapshotForPreview:];
-[UIWebView _webView:previewIsAllowedForPosition:];
-[UIWebView _webView:previewViewControllerForURL:];
-[UIWebView _webView:willPresentPreview:];
-[UIWebView _webViewCommonInitWithWebView:scalesPageToFit:];
-[UIWebView allowsInlineMediaPlayback];
-[UIWebView allowsLinkPreview];
-[UIWebView allowsPictureInPictureMediaPlayback];
-[UIWebView detectsPhoneNumbers];
-[UIWebView keyboardDisplayRequiresUserAction];
-[UIWebView loadData:MIMEType:textEncodingName:baseURL:];
-[UIWebView loadRequest:];
-[UIWebView mediaPlaybackAllowsAirPlay];
-[UIWebView newSnapshotWithRect:];
-[UIWebView pageLength];
-[UIWebView paginationBreakingMode];
-[UIWebView paginationMode];
-[UIWebView restoreStateFromHistoryItem:forWebView:];
-[UIWebView saveStateToHistoryItem:forWebView:];
-[UIWebView scrollViewWasRemoved:];
-[UIWebView setAllowsInlineMediaPlayback:];
-[UIWebView setAllowsLinkPreview:];
-[UIWebView setAllowsPictureInPictureMediaPlayback:];
-[UIWebView setDetectsPhoneNumbers:];
-[UIWebView setGapBetweenPages:];
-[UIWebView setKeyboardDisplayRequiresUserAction:];
-[UIWebView setMediaPlaybackAllowsAirPlay:];
-[UIWebView setMediaPlaybackRequiresUserAction:];
-[UIWebView setPageLength:];
-[UIWebView setPaginationBreakingMode:];
-[UIWebView setPaginationMode:];
-[UIWebView setScalesPageToFit:];
-[UIWebView setSuppressesIncrementalRendering:];
-[UIWebView stringByEvaluatingJavaScriptFromString:];
-[UIWebView suppressesIncrementalRendering];
-[UIWebView view:didSetFrame:oldFrame:];
-[UIWebView webThreadWebView:resource:willSendRequest:redirectResponse:fromDataSource:];
-[UIWebView webView:connectionPropertiesForResource:dataSource:];
-[UIWebView webView:decidePolicyForGeolocationRequestFromOrigin:frame:listener:];
-[UIWebView webView:decidePolicyForNavigationAction:request:frame:decisionListener:];
-[UIWebView webView:decidePolicyForNewWindowAction:request:newFrameName:decisionListener:];
-[UIWebView webView:didChangeLocationWithinPageForFrame:];
-[UIWebView webView:didClearWindowObject:forFrame:];
-[UIWebView webView:didCommitLoadForFrame:];
-[UIWebView webView:didFailLoadWithError:forFrame:];
-[UIWebView webView:didFailProvisionalLoadWithError:forFrame:];
-[UIWebView webView:didFinishLoadForFrame:];
-[UIWebView webView:didFirstLayoutInFrame:];
-[UIWebView webView:didReceiveServerRedirectForProvisionalLoadForFrame:];
-[UIWebView webView:didReceiveTitle:forFrame:];
-[UIWebView webView:didStartProvisionalLoadForFrame:];
-[UIWebView webView:exceededApplicationCacheOriginQuotaForSecurityOrigin:totalSpaceNeeded:];
-[UIWebView webView:frame:exceededDatabaseQuotaForSecurityOrigin:database:];
-[UIWebView webView:identifierForInitialRequest:fromDataSource:];
-[UIWebView webView:printFrameView:];
-[UIWebView webView:resource:canAuthenticateAgainstProtectionSpace:forDataSource:];
-[UIWebView webView:resource:didCancelAuthenticationChallenge:fromDataSource:];
-[UIWebView webView:resource:didFailLoadingWithError:fromDataSource:];
-[UIWebView webView:resource:didFinishLoadingFromDataSource:];
-[UIWebView webView:resource:didReceiveAuthenticationChallenge:fromDataSource:];
-[UIWebView webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:];
-[UIWebView webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:];
-[UIWebView webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:];
-[UIWebView webView:unableToImplementPolicyWithError:frame:];
-[UIWebView webViewClose:];
-[UIWebView webViewMainFrameDidCommitLoad:];
-[UIWebView webViewMainFrameDidFailLoad:withError:];
-[UIWebView webViewMainFrameDidFinishLoad:];
-[UIWebView webViewMainFrameDidFirstVisuallyNonEmptyLayoutInFrame:];
-[UIWebView webViewSupportedOrientationsUpdated:];
```
