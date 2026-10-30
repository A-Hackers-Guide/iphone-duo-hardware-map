# `CAContext`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 21 properties, 65 instance methods, 17 class methods

## Instance variables

```
^v _impl;
@"NSDictionary" _gesturePayload;
```

## Properties

```
@property (TI,R) contextId;
@property (T@"CAHostingToken",R,N) hostingToken;
@property (T@"CALayer",&) layer;
@property (T@"CALayer",&) resizeAnchorContentLayer;
@property (TQ) resizeAnchorContentLayerRenderId;
@property (TI) resizeAnchorContentLayerContextId;
@property (T@"NSDictionary",C) payload;
@property (T@"NSDictionary",C,V_gesturePayload) gesturePayload;
@property (T^{CGColorSpace=}) colorSpace;
@property (TI) commitPriority;
@property (TB) colorMatchUntaggedContent;
@property (T@"NSString",C) contentsFormat;
@property (T@"NSString",C) annotation;
@property (TB) zombifyOnInvalidate;
@property (T@"NSDictionary",R) options;
@property (Tf) level;
@property (TI,R) displayId;
@property (TB,GisSecure) secure;
@property (Tf) desiredDynamicRange;
@property (TB,R) valid;
@property (TI,R,N) commitId;
```

## Class methods

```
+[CAContext currentContext];
+[CAContext setDrawInContextBlock:];
+[CAContext createCacheBlock];
+[CAContext localContext];
+[CAContext drawInContextBlock];
+[CAContext remoteContext];
+[CAContext objectForSlot:];
+[CAContext localContextWithOptions:];
+[CAContext setClientPort:];
+[CAContext allContexts];
+[CAContext setWillSetRootLayerBlock:];
+[CAContext setCreateCacheBlock:];
+[CAContext willSetRootLayerBlock];
+[CAContext setFinalizeContextBlock:];
+[CAContext contextWithId:];
+[CAContext finalizeContextBlock];
+[CAContext remoteContextWithOptions:];
```

## Instance methods

```
-[CAContext valid];
-[CAContext isSecure];
-[CAContext contextId];
-[CAContext setSecure:];
-[CAContext hostingToken];
-[CAContext setColorSpace:];
-[CAContext debugDescription];
-[CAContext layer];
-[CAContext displayId];
-[CAContext dealloc];
-[CAContext payload];
-[CAContext level];
-[CAContext setPayload:];
-[CAContext colorSpace];
-[CAContext invalidate];
-[CAContext setLevel:];
-[CAContext annotation];
-[CAContext setContentsFormat:];
-[CAContext options];
-[CAContext setAnnotation:];
-[CAContext hitTestContext:];
-[CAContext setFence:count:];
-[CAContext createFencePort];
-[CAContext addFence:];
-[CAContext addFence:completion:];
-[CAContext addFence:completionHandler:];
-[CAContext colorMatchUntaggedContent];
-[CAContext commitId];
-[CAContext commitPriority];
-[CAContext contentsFormat];
-[CAContext contextImpl];
-[CAContext createImageSlot:hasAlpha:];
-[CAContext createImageSlot:hasAlpha:extendedColors:];
-[CAContext createSlot];
-[CAContext deleteSlot:];
-[CAContext desiredDynamicRange];
-[CAContext gesturePayload];
-[CAContext initRemoteWithOptions:];
-[CAContext initWithOptions:localContext:];
-[CAContext invalidateFences];
-[CAContext orderAbove:];
-[CAContext orderBelow:];
-[CAContext renderContext];
-[CAContext requestClientGlitch:];
-[CAContext requestServerGlitch:];
-[CAContext resizeAnchorContentLayer];
-[CAContext resizeAnchorContentLayerContextId];
-[CAContext resizeAnchorContentLayerRenderId];
-[CAContext retainRenderContext];
-[CAContext setColorMatchUntaggedContent:];
-[CAContext setCommitPriority:];
-[CAContext setDesiredDynamicRange:];
-[CAContext setFencePort:];
-[CAContext setFencePort:commitHandler:];
-[CAContext setGesturePayload:];
-[CAContext setLayer:];
-[CAContext setObject:forSlot:];
-[CAContext setResizeAnchorContentLayer:];
-[CAContext setResizeAnchorContentLayerContextId:];
-[CAContext setResizeAnchorContentLayerRenderId:];
-[CAContext setZombifyOnInvalidate:];
-[CAContext transferSlot:toContextWithId:];
-[CAContext waitForCommitId:timeout:];
-[CAContext waitForRenderingWithTimeout:];
-[CAContext zombifyOnInvalidate];
```
