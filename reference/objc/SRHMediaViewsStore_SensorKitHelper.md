# `SRHMediaViewsStore`

- Image: [`/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper`](../userland/System__Library__PrivateFrameworks__SensorKitHelper.framework__SensorKitHelper.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
@"NSMapTable" _offScreenMediaViews;
@"NSMapTable" _onScreenMediaViews;
B _connectionDidInvalidate;
@"NSXPCConnection" _connection;
@"NSObject<OS_dispatch_queue>" _q;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (TB,V_connectionDidInvalidate) connectionDidInvalidate;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_q) q;
```

## Class methods

```
+[SRHMediaViewsStore initialize];
```

## Instance methods

```
-[SRHMediaViewsStore setupConnection];
-[SRHMediaViewsStore initWithScrollView:];
-[SRHMediaViewsStore dealloc];
-[SRHMediaViewsStore connection];
-[SRHMediaViewsStore setConnection:];
-[SRHMediaViewsStore q];
-[SRHMediaViewsStore setQ:];
-[SRHMediaViewsStore connectionDidInvalidate];
-[SRHMediaViewsStore setConnectionDidInvalidate:];
-[SRHMediaViewsStore addViewToStore:];
-[SRHMediaViewsStore _writeMediaEventsToBiome:];
-[SRHMediaViewsStore markViewsAsOffScreen];
-[SRHMediaViewsStore markViewsAsOnScreen];
-[SRHMediaViewsStore processScrollViewOffset];
-[SRHMediaViewsStore removeAllViews];
-[SRHMediaViewsStore removeViewFromStore:];
-[SRHMediaViewsStore scrollViewVisibleArea];
```
