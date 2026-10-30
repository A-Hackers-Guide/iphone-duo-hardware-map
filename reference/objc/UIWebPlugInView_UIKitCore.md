# `UIWebPlugInView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAKView`
- 9 instance variables, 4 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"UIWebDocumentView" _webView;
@"CALayer" _hostingLayer;
@"UIView" _uiView;
^{__CFRunLoopObserver=} _mainRunLoopDrawObserver;
B _isFullScreen;
B _parentedInLayer;
B _isQuickTimePlugIn;
B _isMapViewPlugIn;
B _isiAdPlugIn;
```

## Properties

```
@property (TB,N,GisParentedInLayer,V_parentedInLayer) parentedInLayer;
@property (TB,N,V_isQuickTimePlugIn) isQuickTimePlugIn;
@property (TB,N,V_isMapViewPlugIn) isMapViewPlugIn;
@property (TB,N,V_isiAdPlugIn) isiAdPlugIn;
```

## Instance methods

```
-[UIWebPlugInView viewDidMoveToWindow];
-[UIWebPlugInView dealloc];
-[UIWebPlugInView drawRect:];
-[UIWebPlugInView setFrame:];
-[UIWebPlugInView methodSignatureForSelector:];
-[UIWebPlugInView layout];
-[UIWebPlugInView respondsToSelector:];
-[UIWebPlugInView forwardInvocation:];
-[UIWebPlugInView setFrameSize:];
-[UIWebPlugInView isMapViewPlugIn];
-[UIWebPlugInView reshape];
-[UIWebPlugInView setIsiAdPlugIn:];
-[UIWebPlugInView _attachPluginLayerOnMainThread];
-[UIWebPlugInView _connectPluginLayers];
-[UIWebPlugInView _detachPluginLayerOnMainThread];
-[UIWebPlugInView _disconnectPluginLayers];
-[UIWebPlugInView _reshapeOnMainThread];
-[UIWebPlugInView _viewDidMoveToWindowOnMainThread];
-[UIWebPlugInView attachPluginLayer];
-[UIWebPlugInView detachPluginLayer];
-[UIWebPlugInView initWithWebView:plugInView:];
-[UIWebPlugInView invalidateGState];
-[UIWebPlugInView isParented];
-[UIWebPlugInView isParentedInLayer];
-[UIWebPlugInView isQuickTimePlugIn];
-[UIWebPlugInView isiAdPlugIn];
-[UIWebPlugInView mouseDown:];
-[UIWebPlugInView mouseUp:];
-[UIWebPlugInView objectForWebScript];
-[UIWebPlugInView plugInView];
-[UIWebPlugInView pluginLayer];
-[UIWebPlugInView setIsMapViewPlugIn:];
-[UIWebPlugInView setIsQuickTimePlugIn:];
-[UIWebPlugInView setParentedInLayer:];
-[UIWebPlugInView setWebView:];
-[UIWebPlugInView webPlugInDestroy];
-[UIWebPlugInView webPlugInInitialize];
-[UIWebPlugInView webPlugInStart];
-[UIWebPlugInView webPlugInStop];
-[UIWebPlugInView willProvidePluginLayer];
```
