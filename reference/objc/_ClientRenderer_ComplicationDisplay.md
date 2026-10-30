# `_ClientRenderer`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"CDComplicationHostingView" _host;
d _renderTime;
d _renderCost;
@"NSObject<OS_dispatch_semaphore>" _sema;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[_ClientRenderer init];
-[_ClientRenderer renderWithViewData:scale:handler:];
-[_ClientRenderer _handleRenderStatsTime:cost:];
```
