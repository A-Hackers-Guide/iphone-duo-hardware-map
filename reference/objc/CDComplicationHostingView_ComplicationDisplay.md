# `CDComplicationHostingView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CLKMonochromeComplicationView`
- 1 instance variables, 12 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"_TtC19ComplicationDisplay20_ComplicationHosting" _hosting;
```

## Properties

```
@property (T@"_TtC19ComplicationDisplay20_ComplicationHosting",R,N,V_hosting) hosting;
@property (TB,R,N) rendersAsynchronously;
@property (T@?,C,N) renderStatsHandler;
@property (TB,N) shouldCallRenderStatsHandlerOnMainQueue;
@property (TB,N) shouldAccentDesaturatedView;
@property (T@"NSData",C,N) viewData;
@property (TB,N) paused;
@property (T@"<CLKMonochromeFilterProvider>",W,N) filterProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CDComplicationHostingView async];
+[CDComplicationHostingView sync];
```

## Instance methods

```
-[CDComplicationHostingView hosting];
-[CDComplicationHostingView rendersAsynchronously];
-[CDComplicationHostingView paused];
-[CDComplicationHostingView setBounds:];
-[CDComplicationHostingView sizeThatFits:];
-[CDComplicationHostingView setPaused:];
-[CDComplicationHostingView setFrame:];
-[CDComplicationHostingView initWithFrame:];
-[CDComplicationHostingView viewData];
-[CDComplicationHostingView setShouldAccentDesaturatedView:];
-[CDComplicationHostingView filterProvider];
-[CDComplicationHostingView renderStatsHandler];
-[CDComplicationHostingView setFilterProvider:];
-[CDComplicationHostingView setRenderStatsHandler:];
-[CDComplicationHostingView setViewData:];
-[CDComplicationHostingView transitionToMonochromeWithFraction:];
-[CDComplicationHostingView updateMonochromeColor];
-[CDComplicationHostingView initWithFrame:async:];
-[CDComplicationHostingView setShouldCallRenderStatsHandlerOnMainQueue:];
-[CDComplicationHostingView shouldAccentDesaturatedView];
-[CDComplicationHostingView shouldCallRenderStatsHandlerOnMainQueue];
-[CDComplicationHostingView waitForAsyncRendering];
```
