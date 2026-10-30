# `_UILibArchiveStreamingReader`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
q _state;
^{ui_archive=} _laArchive;
i _laArchiveType;
@"NSString" _laArchiveTypeName;
i _laProcessingState;
q _nextLoadedItemEntrySequenceIndex;
@"NSMutableArray" _readableLoadedItemEntryQueue;
@"NSError" _readError;
@"NSString" _archivePath;
^{ui_archive=} _underlyingArchive;
q _appleDoubleIdentificationType;
```

## Properties

```
@property (T@"NSString",R,N,V_archivePath) archivePath;
@property (T^{ui_archive=},R,N,V_underlyingArchive) underlyingArchive;
@property (Tq,N,V_appleDoubleIdentificationType) appleDoubleIdentificationType;
@property (T@"NSString",R,N) openedArchiveUnderlyingFormatName;
```

## Instance methods

```
-[_UILibArchiveStreamingReader open];
-[_UILibArchiveStreamingReader close];
-[_UILibArchiveStreamingReader _closeArchive];
-[_UILibArchiveStreamingReader _debugLoadAndPrintAllRemainingItems];
-[_UILibArchiveStreamingReader _loadItemByReadingAttributesFromUnderlyingArchiveEntry:];
-[_UILibArchiveStreamingReader _nextSimpleItemFromPendingQueueOrLibArchiveRead];
-[_UILibArchiveStreamingReader _openArchive];
-[_UILibArchiveStreamingReader _readItemsWithShouldVisitBlock:visitorBlock:error:];
-[_UILibArchiveStreamingReader _shouldReportAsAppleDoubleItem:withConfirmedAppleDoubleFiles:];
-[_UILibArchiveStreamingReader _shouldReportAsLogicalItem:withConfirmedAppleDoubleFiles:];
-[_UILibArchiveStreamingReader appleDoubleIdentificationType];
-[_UILibArchiveStreamingReader archivePath];
-[_UILibArchiveStreamingReader initForReadingArchivePath:];
-[_UILibArchiveStreamingReader openedArchiveUnderlyingFormatName];
-[_UILibArchiveStreamingReader readAllItemsWithBlock:error:];
-[_UILibArchiveStreamingReader readLogicalItemsWithBlock:error:];
-[_UILibArchiveStreamingReader setAppleDoubleIdentificationType:];
-[_UILibArchiveStreamingReader underlyingArchive];
```
