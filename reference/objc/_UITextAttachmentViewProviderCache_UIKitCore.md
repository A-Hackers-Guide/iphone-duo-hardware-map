# `_UITextAttachmentViewProviderCache`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _registeredViewProviderReusePolicies;
@"NSMapTable" _textAttachmentToViewProvidersCacheTableForEditingPolicy;
@"NSMapTable" _viewProviderToStateCacheTableForEditingPolicy;
@"NSMapTable" _layoutFragmentToStateCacheTableForScrollingPolicy;
@"NSMapTable" _viewProviderToStateCacheTableForScrollingPolicy;
```

## Instance methods

```
-[_UITextAttachmentViewProviderCache _pushRenderingSurfaceView:forLayoutFragment:];
-[_UITextAttachmentViewProviderCache _popScrollingPolicyRenderingSurfaceViewForLayoutFragment:];
-[_UITextAttachmentViewProviderCache init];
-[_UITextAttachmentViewProviderCache _invalidateForScrollingPolicyLayoutFragmentForViewProvider:];
-[_UITextAttachmentViewProviderCache cacheRenderingSurface:forKey:];
-[_UITextAttachmentViewProviderCache addTextAttachmentViewProvider:forTextAttachment:];
-[_UITextAttachmentViewProviderCache retrieveCachedRenderingSurfaceForKey:];
-[_UITextAttachmentViewProviderCache _invalidateForEditingPolicyLayoutFragmentForViewProvider:];
-[_UITextAttachmentViewProviderCache registerTextAttachmentViewProviderReusePolicy:forTextAttachmentViewProviderType:];
-[_UITextAttachmentViewProviderCache nextTextAttachmentViewProviderForTextAttachment:];
-[_UITextAttachmentViewProviderCache _pushTextAttachmentViewProvider:forTextAttachment:];
-[_UITextAttachmentViewProviderCache _popTextAttachmentViewProviderForTextAttachment:];
-[_UITextAttachmentViewProviderCache _popEditingPolicyRenderingSurfaceViewForLayoutFragment:];
-[_UITextAttachmentViewProviderCache _clearAllCacheTables];
-[_UITextAttachmentViewProviderCache _reusePolicyForViewProvider:];
```
