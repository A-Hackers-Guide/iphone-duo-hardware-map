# `FBSApplicationLibraryConfiguration`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _personaAware;
B _allowConcurrentLoading;
# _applicationInfoClass;
# _applicationPlaceholderClass;
@? _installedApplicationFilter;
@? _placeholderFilter;
@? _applicationIdentityFilter;
@? _placeholderIdentityFilter;
```

## Properties

```
@property (T#,&,N,V_applicationInfoClass) applicationInfoClass;
@property (T#,&,N,V_applicationPlaceholderClass) applicationPlaceholderClass;
@property (TB,N,V_allowConcurrentLoading) allowConcurrentLoading;
@property (TB,N,GisPersonaAware,V_personaAware) personaAware;
@property (T@?,C,N,V_installedApplicationFilter) installedApplicationFilter;
@property (T@?,C,N,V_placeholderFilter) placeholderFilter;
@property (T@?,C,N,V_applicationIdentityFilter) applicationIdentityFilter;
@property (T@?,C,N,V_placeholderIdentityFilter) placeholderIdentityFilter;
```

## Instance methods

```
-[FBSApplicationLibraryConfiguration init];
-[FBSApplicationLibraryConfiguration copyWithZone:];
-[FBSApplicationLibraryConfiguration setApplicationPlaceholderClass:];
-[FBSApplicationLibraryConfiguration allowConcurrentLoading];
-[FBSApplicationLibraryConfiguration applicationIdentityFilter];
-[FBSApplicationLibraryConfiguration applicationInfoClass];
-[FBSApplicationLibraryConfiguration applicationPlaceholderClass];
-[FBSApplicationLibraryConfiguration installedApplicationFilter];
-[FBSApplicationLibraryConfiguration isPersonaAware];
-[FBSApplicationLibraryConfiguration placeholderFilter];
-[FBSApplicationLibraryConfiguration placeholderIdentityFilter];
-[FBSApplicationLibraryConfiguration setAllowConcurrentLoading:];
-[FBSApplicationLibraryConfiguration setApplicationIdentityFilter:];
-[FBSApplicationLibraryConfiguration setApplicationInfoClass:];
-[FBSApplicationLibraryConfiguration setInstalledApplicationFilter:];
-[FBSApplicationLibraryConfiguration setPersonaAware:];
-[FBSApplicationLibraryConfiguration setPlaceholderFilter:];
-[FBSApplicationLibraryConfiguration setPlaceholderIdentityFilter:];
```
