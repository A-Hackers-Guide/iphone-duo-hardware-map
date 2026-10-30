# `_TtC19ComplicationDisplay20_ComplicationHosting`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLKMonochromeComplicationView`
- 13 instance variables, 9 properties, 24 instance methods, 2 class methods

## Instance variables

```
(objc_protocol 0x25b095278) ? filterProvider;
Swift.Bool inPreview;
ComplicationDisplay.MonochromeModel model;
Swift.Bool isMonochrome;
SwiftUI._UIHostingViewable _$s_So16UIViewControllerCXc hostingViewController;
_$sSo6UIViewC view;
Swift.Bool rendersAsynchronously;
_$sySd_SdtcSg renderStatsHandler;
Swift.Bool shouldCallRenderStatsHandlerOnMainQueue;
Swift.Bool shouldAccentDesaturatedView;
Swift.Bool supportsComplicationForeground;
Foundation.Data ? viewData;
Swift.Bool paused;
```

## Properties

```
@property (T@"<CLKMonochromeFilterProvider>",N,W,VfilterProvider) filterProvider;
@property (T@"UIView",N,R,Vview) view;
@property (TB,N,R,VrendersAsynchronously) rendersAsynchronously;
@property (T@?,N,C) renderStatsHandler;
@property (TB,N,VshouldCallRenderStatsHandlerOnMainQueue) shouldCallRenderStatsHandlerOnMainQueue;
@property (TB,N,VshouldAccentDesaturatedView) shouldAccentDesaturatedView;
@property (TB,N,VsupportsComplicationForeground) supportsComplicationForeground;
@property (T@"NSData",N,C) viewData;
@property (TB,N,Vpaused) paused;
```

## Class methods

```
+[_TtC19ComplicationDisplay20_ComplicationHosting async];
+[_TtC19ComplicationDisplay20_ComplicationHosting sync];
```

## Instance methods

```
-[_TtC19ComplicationDisplay20_ComplicationHosting rendersAsynchronously];
-[_TtC19ComplicationDisplay20_ComplicationHosting paused];
-[_TtC19ComplicationDisplay20_ComplicationHosting init];
-[_TtC19ComplicationDisplay20_ComplicationHosting dealloc];
-[_TtC19ComplicationDisplay20_ComplicationHosting sizeThatFits:];
-[_TtC19ComplicationDisplay20_ComplicationHosting view];
-[_TtC19ComplicationDisplay20_ComplicationHosting setPaused:];
-[_TtC19ComplicationDisplay20_ComplicationHosting initWithCoder:];
-[_TtC19ComplicationDisplay20_ComplicationHosting viewData];
-[_TtC19ComplicationDisplay20_ComplicationHosting setShouldAccentDesaturatedView:];
-[_TtC19ComplicationDisplay20_ComplicationHosting filterProvider];
-[_TtC19ComplicationDisplay20_ComplicationHosting renderStatsHandler];
-[_TtC19ComplicationDisplay20_ComplicationHosting setFilterProvider:];
-[_TtC19ComplicationDisplay20_ComplicationHosting setRenderStatsHandler:];
-[_TtC19ComplicationDisplay20_ComplicationHosting setViewData:];
-[_TtC19ComplicationDisplay20_ComplicationHosting transitionToMonochromeWithFraction:];
-[_TtC19ComplicationDisplay20_ComplicationHosting updateMonochromeColor];
-[_TtC19ComplicationDisplay20_ComplicationHosting initWithFrame:async:];
-[_TtC19ComplicationDisplay20_ComplicationHosting setShouldCallRenderStatsHandlerOnMainQueue:];
-[_TtC19ComplicationDisplay20_ComplicationHosting setSupportsComplicationForeground:];
-[_TtC19ComplicationDisplay20_ComplicationHosting shouldAccentDesaturatedView];
-[_TtC19ComplicationDisplay20_ComplicationHosting shouldCallRenderStatsHandlerOnMainQueue];
-[_TtC19ComplicationDisplay20_ComplicationHosting supportsComplicationForeground];
-[_TtC19ComplicationDisplay20_ComplicationHosting waitForAsyncRendering];
```
