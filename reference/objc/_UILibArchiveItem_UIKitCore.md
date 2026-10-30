# `_UILibArchiveItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIArchiveItem`
- 2 instance variables, 2 properties, 2 instance methods, 1 class methods

## Instance variables

```
^{ui_archive_entry=} _underlyingArchiveEntry;
^{ui_archive=} _underlyingArchive;
```

## Properties

```
@property (T^{ui_archive_entry=},R,V_underlyingArchiveEntry) underlyingArchiveEntry;
@property (T^{ui_archive=},R,V_underlyingArchive) underlyingArchive;
```

## Class methods

```
+[_UILibArchiveItem itemByReadingAttributesFromUnderlyingArchiveEntry:archive:];
```

## Instance methods

```
-[_UILibArchiveItem underlyingArchive];
-[_UILibArchiveItem underlyingArchiveEntry];
```
