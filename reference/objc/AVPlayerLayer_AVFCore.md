# `AVPlayerLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `AVKeyPathDependencyHost`, `AVWeakObservable`
- 2 instance variables, 11 properties, 156 instance methods, 5 class methods

## Instance variables

```
@"AVPlayerLayerInternal" _playerLayer;
{CGPoint="x"d"y"d} __captionPreviewPosition;
```

## Properties

```
@property (T{CGPoint=dd},N,V__captionPreviewPosition) _captionPreviewPosition;
@property (TB,N,S_setUseInterstitialLayerForVideoRect:) _useInterstitialLayerForVideoRect;
@property (T@"AVPlayer",&,N) player;
@property (T@"NSString",C) videoGravity;
@property (TB,R,N,GisReadyForDisplay) readyForDisplay;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) videoRect;
@property (T@"NSDictionary",C,N) pixelBufferAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVPlayerLayer playerLayerWithPlayer:];
+[AVPlayerLayer makeClosedCaptionLayer];
+[AVPlayerLayer keyPathsForValuesAffectingVideoRect];
+[AVPlayerLayer keyPathsForValuesAffecting_presentationSize];
+[AVPlayerLayer _swapSublayersBetweenPlayerLayer:andPlayerLayer:];
```

## Instance methods

```
-[AVPlayerLayer pixelBufferAttributes];
-[AVPlayerLayer setToneMapToStandardDynamicRange:];
-[AVPlayerLayer player];
-[AVPlayerLayer _addBoundsAnimationToLayer:usingAnimation:forKey:];
-[AVPlayerLayer setPixelBufferAttributes:];
-[AVPlayerLayer observeValueForKeyPath:ofObject:change:context:];
-[AVPlayerLayer isOverscanSubtitleSupportEnabled];
-[AVPlayerLayer setCaptionPreviewProfileID:position:text:];
-[AVPlayerLayer setPreferredDynamicRange:];
-[AVPlayerLayer isReadyForDisplay];
-[AVPlayerLayer videoPerformanceMetrics];
-[AVPlayerLayer init];
-[AVPlayerLayer stopShowingCaptionPreview];
-[AVPlayerLayer dealloc];
-[AVPlayerLayer addAnimation:forKey:];
-[AVPlayerLayer initWithLayer:];
-[AVPlayerLayer setBounds:];
-[AVPlayerLayer setPlayer:];
-[AVPlayerLayer removeFromSuperlayer];
-[AVPlayerLayer legibleContentInsets];
-[AVPlayerLayer layerDidBecomeVisible:];
-[AVPlayerLayer addSublayer:];
-[AVPlayerLayer _addPositionAnimationToLayer:usingAnimation:forKey:];
-[AVPlayerLayer removeAllAnimations];
-[AVPlayerLayer setContentsScale:];
-[AVPlayerLayer _nameForLogging];
-[AVPlayerLayer setOverscanSubtitleSupportEnabled:];
-[AVPlayerLayer videoGravity];
-[AVPlayerLayer removeAnimationForKey:];
-[AVPlayerLayer insertSublayer:above:];
-[AVPlayerLayer layoutSublayers];
-[AVPlayerLayer videoRect];
-[AVPlayerLayer insertSublayer:atIndex:];
-[AVPlayerLayer setVideoGravity:];
-[AVPlayerLayer replaceSublayer:with:];
-[AVPlayerLayer setLegibleContentInsets:];
-[AVPlayerLayer _STSLabel];
-[AVPlayerLayer copyDisplayedPixelBuffer];
-[AVPlayerLayer insertSublayer:below:];
-[AVPlayerLayer setSublayers:];
-[AVPlayerLayer _maskLayer];
-[AVPlayerLayer _leaveSecondScreenModeForLayer:];
-[AVPlayerLayer _updateReadyForDisplayOnMainQueue:skipInformingParent:forceKVO:];
-[AVPlayerLayer _windowSceneDidEnterBackground:];
-[AVPlayerLayer playerPublisher];
-[AVPlayerLayer _configurePlayerWhenEnteringPIP];
-[AVPlayerLayer _currentWindowSceneIsForeground];
-[AVPlayerLayer _windowSceneWillEnterForeground];
-[AVPlayerLayer _activeMode];
-[AVPlayerLayer _addAnimationsForClosedCaptionLayer:gravity:forKey:];
-[AVPlayerLayer _addAnimationsForInterstitialLayer:forKey:];
-[AVPlayerLayer _addAnimationsForMaskLayer:forKey:];
-[AVPlayerLayer _addAnimationsForPIPPlaceholderLayer:forKey:];
-[AVPlayerLayer _addAnimationsForVideoLayer:size:gravity:forKey:];
-[AVPlayerLayer _addObserversForVideoLayer:];
-[AVPlayerLayer _addSublayerTransformAnimationToLayer:fromTransform:usingAnimation:gravity:presentationSize:forKey:];
-[AVPlayerLayer _applyCurrentItemPresentationSizeChangeAndForceUpdate:];
-[AVPlayerLayer _applyPresentationSizeChange:andForceUpdate:];
-[AVPlayerLayer _associateWithLayer:forMode:];
-[AVPlayerLayer _associatedRemoteModeLayer];
-[AVPlayerLayer _cancelScheduledInterstitialVisibilityUpdate];
-[AVPlayerLayer _captionPreviewPosition];
-[AVPlayerLayer _closedCaptionLayer];
-[AVPlayerLayer _commitTimedCATransactionToUpdateVisibilityOfInterstitialLayer:maskLayer:toShowInterstitial:atCAMediaTime:];
-[AVPlayerLayer _configurePlayerWhenLeavingPIP];
-[AVPlayerLayer _currentWindowSceneIsForegroundDefault];
-[AVPlayerLayer _disassociateWithLayerForMode:];
-[AVPlayerLayer _displaySize_invokeOnMainQueue];
-[AVPlayerLayer _ensureSubtitlePreviewLayer];
-[AVPlayerLayer _enterPIPModeRedirectingVideoToLayer:];
-[AVPlayerLayer _enterSecondScreenModeRedirectingVideoToLayer:];
-[AVPlayerLayer _forBoundsAnimations:applyBlock:];
-[AVPlayerLayer _forceLayout];
-[AVPlayerLayer _forceWindowSceneEvent:];
-[AVPlayerLayer _getMaskLayer:videoLayer:subtitleLayer:subtitlePreviewLayer:closedCaptionLayer:interstitialLayer:];
-[AVPlayerLayer _handleIsDisplayingClosedCaptionsDidChange:player:];
-[AVPlayerLayer _handleNonForcedSubtitleDisplayDidChange:player:];
-[AVPlayerLayer _handlePlayerCurrentItemDidChangeForPlayer:];
-[AVPlayerLayer _interstitialLayer];
-[AVPlayerLayer _interstitialLayerIsVisible];
-[AVPlayerLayer _isConnectedToSecondScreen];
-[AVPlayerLayer _isPartOfForegroundScene];
-[AVPlayerLayer _leavePIPModeForLayer:];
-[AVPlayerLayer _mergeClientLayersIntoMaskLayer:];
-[AVPlayerLayer _notifyPlayerOfDisplaySize];
-[AVPlayerLayer _notifyPlayerOfLayerForegroundStateChange];
-[AVPlayerLayer _overridesPreferredDynamicRangeForVideo];
-[AVPlayerLayer _percentCoverageRelativeToRootLayer_invokeOnMainQueue];
-[AVPlayerLayer _preferredDynamicRangeForPiP];
-[AVPlayerLayer _presentationSize];
-[AVPlayerLayer _preventsChangesToSublayerHierarchy];
-[AVPlayerLayer _removeObserversForVideoLayer:];
-[AVPlayerLayer _restoreClientLayers:intoMaskLayer:];
-[AVPlayerLayer _scheduleTimerToUpdateVisibilityOfInterstitialLayer:maskLayer:toShowInterstitial:atDispatchTime:atCAMediaTime:];
-[AVPlayerLayer _setCaptionPreviewPosition:];
-[AVPlayerLayer _setIsConnectedToSecondScreen:];
-[AVPlayerLayer _setIsPartOfForegroundScene:];
-[AVPlayerLayer _setOverridesPreferredDynamicRangeForVideo:];
-[AVPlayerLayer _setPlayer:forPIP:];
-[AVPlayerLayer _setPreventsChangesToSublayerHierarchy:];
-[AVPlayerLayer _setShowInterstitialInstead:];
-[AVPlayerLayer _setShowInterstitialInstead:afterDelay:];
-[AVPlayerLayer _setSublayersForPIP:];
-[AVPlayerLayer _setSublayersForPIP:updateReadyForDisplay:];
-[AVPlayerLayer _setSublayersPreventChangesToSublayerHierarchy:];
-[AVPlayerLayer _setSubtitlePreviewHelper:];
-[AVPlayerLayer _setUseInterstitialLayerForVideoRect:];
-[AVPlayerLayer _setWillManageSublayersAsSwappedLayers:];
-[AVPlayerLayer _showInterstitialInstead];
-[AVPlayerLayer _startObservingPlayer:];
-[AVPlayerLayer _stashClientLayers];
-[AVPlayerLayer _stopObservingPlayer:];
-[AVPlayerLayer _sublayersForPIP];
-[AVPlayerLayer _subtitleLayer];
-[AVPlayerLayer _subtitlePreviewHelper];
-[AVPlayerLayer _subtitlePreviewLayer];
-[AVPlayerLayer _unstashClientLayers];
-[AVPlayerLayer _updateIsPartOfForegroundScene];
-[AVPlayerLayer _updatePreferredDynamicRangeWithAnimation:];
-[AVPlayerLayer _updateReadyForDisplay:];
-[AVPlayerLayer _updateReadyForDisplay:forceKVO:];
-[AVPlayerLayer _updateReadyForDisplay:skipInformingParent:];
-[AVPlayerLayer _updateReadyForDisplay:skipInformingParent:forceKVO:];
-[AVPlayerLayer _updateReadyForDisplayForPlayerCurrentItem];
-[AVPlayerLayer _updateReadyForDisplayForPlayerCurrentItemAndForceKVO:];
-[AVPlayerLayer _updateSubtitlePreviewLayerImage];
-[AVPlayerLayer _useInterstitialLayerForVideoRect];
-[AVPlayerLayer _videoLayer];
-[AVPlayerLayer _videoRectForBounds:];
-[AVPlayerLayer _willManageSublayersAsSwappedLayers];
-[AVPlayerLayer _windowSceneDidEnterBackground];
-[AVPlayerLayer _windowSceneWillEnterForeground:];
-[AVPlayerLayer addCallbackToCancelDuringDeallocation:];
-[AVPlayerLayer aspectRatioMatchesInterstitialLayer:];
-[AVPlayerLayer declareKeyPathDependenciesWithRegistry:];
-[AVPlayerLayer enterPIPModeRedirectingVideoToLayer:];
-[AVPlayerLayer hasEnqueuedVideoFrameChanged:];
-[AVPlayerLayer isForScrubbingOnly];
-[AVPlayerLayer isLanczosFilterDownscalingEnabled];
-[AVPlayerLayer isLegibleDisplayEnabled];
-[AVPlayerLayer isPIPModeEnabled];
-[AVPlayerLayer lanczosFilterDownscaleFactor];
-[AVPlayerLayer leavePIPMode];
-[AVPlayerLayer placeholderContentLayerDuringPIPMode];
-[AVPlayerLayer setForScrubbingOnly:];
-[AVPlayerLayer setLanczosFilterDownscaleFactor:];
-[AVPlayerLayer setLanczosFilterDownscalingEnabled:];
-[AVPlayerLayer setLegibleDisplayEnabled:];
-[AVPlayerLayer setPIPModeEnabled:];
-[AVPlayerLayer setPlaceholderContentLayerDuringPIPMode:];
-[AVPlayerLayer setSignalsVideoRectChangeBeforeChangingContentsAspectRatio:];
-[AVPlayerLayer set_captionPreviewPosition:];
-[AVPlayerLayer signalsVideoRectChangeBeforeChangingContentsAspectRatio];
-[AVPlayerLayer startRedirectingVideoToLayer:forMode:];
-[AVPlayerLayer stopRedirectingVideoToLayer:];
-[AVPlayerLayer updateVisibilityOfInterstitialLayer:maskLayer:toShowInterstitial:];
```
