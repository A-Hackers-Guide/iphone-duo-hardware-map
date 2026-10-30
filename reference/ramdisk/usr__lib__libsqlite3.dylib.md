# `/usr/lib/libsqlite3.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,047,680 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 2408)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (2)

- `/usr/lib/libsqlite3.dylib (compatibility version 9.0.0, current version 408.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (2,410)

```
no such database: %s
SELECT %s FROM %s T WHERE T.%Q <= ? AND T.%Q >= ? ORDER BY T.%Q DESC
CREATE TABLE \"%w\".\"%w_rowid\"(rowid INTEGER PRIMARY KEY,nodeno
ok
'%s' is not a function
ousli
SQLITE_
array
 WHERE <expr>
json_group_object
'delete' may not be used with a contentless_delete=1 table
DELETE FROM main.
%s_%02d.db
fcntl
AutoCommit
DropTable
rwc
contentless_delete=1 requires a contentless table
fts5vocab
Sort
journal_size_limit
hex
k(%d
rows deleted
locking protocol
,%s(x.'c%d%q')
%z, 'c%d%q'
PRAGMA %Q.data_version
seekAndWrite: updated file size hint from %lld to actual size %lld
RealAffinity
cannot VACUUM from within a transaction
p1
integer
name
JSON path too deep
count
seekAndRead
FOREIGN KEY constraint failed
 USING 
alg
unindexed
phrase
GROUP
after drop column
pm
simple
DROP TABLE IF EXISTS %Q.'%q_segments';DROP TABLE IF EXISTS %Q.'%q_segdir';DROP TABLE IF EXISTS %Q.'%q_docsize';DROP TABLE IF EXISTS %Q.'%q_stat';%s DROP TABLE IF EXISTS %Q.'%q_content';
UTF8
DELETE FROM %Q.'%q_segdir'
%s_stat
MAX_EXPR_DEPTH=1000
compression_stream_process alpha failed for %d\n
failed to get page %u
aggregate functions are not allowed in the GROUP BY clause
target object/alias may not appear in FROM clause: %s
DELETE FROM %Q.%s
Mapping (%lld -> %lld) missing from %s table
ENABLE_SESSION
SQLITE_EXEMPT_PATH_FROM_VNODE_GUARDS
unsafe use of %#T()
thstndrd
mediaanalysisd
at most %d tables in a join
RETURNING may not use \"TABLE.*\" wildcards
%03d
compress
segdir
fts5: error creating shadow table %q_%s: %s
last read ended with return %ld with errno %d\n
CREATE TABLE x(value,pointer hidden,count hidden,ctype hidden)
%s=?
shadow
SELECT * FROM \"%w\".\"%w_rowid\" WHERE rowid=?1
bind on a busy prepared statement: [%s]
SNaN
,\n  
too many arguments on %s() - max %d
wrong # of entries in index 
log10
}
prefix length out of range (max 999)
Rowid %lld out of order
cannot VACUUM - SQL statements in progress
origin
USING ROWID SEARCH ON TABLE %s FOR IN-OPERATOR
%04d-%02d-%02d
SELECT %s WHERE rowid=?
, NULL
unix-dotfile
concat_ws
pgsz
tional
undersize RTree blobs in \"%q_node\"
unicode
HAS_CODEC_RESTRICTED
invalid change: %s value in PK of old.* record
json_pretty
tclsh
SQLITE_ENABLE_FILE_ASSERTIONS
sqlite_rename_quotefix
fts5: corrupt structure record for table \"%s\"
compression_stream_process bravo failed for %d\n
IfNullRow
index corruption
SpringBoard
size
shrink_memory
(\"%s\"
UPDATE
table
Integrity check failed: %s
USE TEMP B-TREE FOR LAST %d TERMS OF ORDER BY
no such constraint: %s
no such column: \"%T\"
asc
RtreeMatchArg
INSERT INTO main.
/iTunes/MediaLibrary.sqlitedb
BEGIN DEFERRED; PRAGMA schema_version; COMMIT;
foreign_key_check
timeout
REUSE LIST SUBQUERY %d
%02d:%02d:%02d
file renamed while open: %s
unixShmMap-write
recursive reference in a subquery: %s
UTF-16be
CREATE TABLE %Q.%s(%s)
%.*s, %s%s
ence
Next
VColumn
argument type mismatch
sqllogOpenlog(): Failed to open log file
/NoteStore.sqlite
Real
short_column_names
generated columns cannot be part of the PRIMARY KEY
degrees
segments
(join-%u)
PerfPowerServices
non-unique entry in index 
ESCAPE expression must be a single character
->>
<dst path null>
regexp
UTF16le
trunc
ftruncate
sqlite_temp_schema
%s.%s.%s
NEAR
TEMP_STORE=1
wr
alize
always
cache
virtual table
DESC
-shm
fts5 expression tree is too large (maximum depth %d)
seq
FILTER may not be used with non-aggregate %#T()
expressions
zeroblob
weekday 
another row available
IdxGE
Le
@
OR
multiple tokenize=... directives
CursorUnlock
variable number must be between ?1 and ?%d
percentile
id INTEGER PRIMARY KEY, sz BLOB
?%d
floor
SELECT k, v FROM %Q.'%q_config'
NoConflict
python
a CHECK constraint
fts3tokenize
reserved fts5 column name: %s
REPLACE INTO %Q.'%q_docsize' VALUES(?,?%s)
pragma application_id = %d;\n
.0
wal_autocheckpoint
builtin
affinity
Found (%lld -> %lld) in %s table, expected (%lld -> %lld)
MAX_LENGTH=2147483645
MAX_PAGE_SIZE=65536
pragma page_size
database corruption page %u of %s
OpenAutoindex
CREATE TABLE x
UPDATE \"%w\".sqlite_sequence set name = %Q WHERE name = %Q
JSON cannot hold BLOB values
langid
vtable constructor called recursively: %s
rowid=?
filename
-Inf
 AND (?
must specify either filename= or data= but not both
LZMA
-- %s
rename
HAVING clause on a non-aggregate query
name=%Q AND sql=%Q
SQLITE_SQLLOG_CONDITIONAL
rowid
Tree %u page %u cell %u: 
ATTACH %Q AS %s
access to %z is prohibited
sqlite_fail
,\n
icate
invalid change: column %d is undefined
SELECT sql FROM sqlite_schema WHERE sql NOT NULL AND type IN ('index','trigger','view')
use DROP TABLE to delete table %s
cannot detach database %s
 NULL
compression_stream_process failed for %d\n
PRAGMA \"%w\".page_count
UPDATE \"%w\".sqlite_master SET sql = sqlite_rename_quotefix(%Q, sql)WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X' AND sql NOT LIKE 'create virtual%%'
sqlite3_get_table() called with two or more incompatible queries
%sSCALAR SUBQUERY %d
%s.idx
read error (len %d)
real
application_id
no such column: %s
too many prefix indexes (max %d)
securityd
radians
notindexed
?1, (CASE WHEN ?2=X'' THEN NULL ELSE ?2 END)
/*scan*/
SetSubtype
1
int64
cannot use window functions in recursive queries
C
Insert
ruby
max_page_count
wdth
backupd
isisi
bm25
readlink
int32
ceiling
queries
IsTrue
RowData
ATOMIC_INTRINSICS=1
cannot limit WAL size: %s
Divide
malformed contentless_delete=... directive
IfNot
ANY
cos
%#Q
ator
hexkey
CREATE VIRTUAL TABLE
cannot commit transaction - SQL statements in progress
freelist_count
local time unavailable
, T.c%d
corespeechd
Yield
sqlite_master
CREATE %s %.*s
unistr_quote
fts4aux
malformed inverted index for FTS5 table %s.%s
set list
too many references to \"%s\": max 65535
index
malformed inverted index for FTS%d table %s.%s
/* unknown trigger */ 
flags
 values differ from index 
%s mode not allowed: %s
database %s is locked
instance
pragma journal_mode = wal
secure_delete
UPDATE temp.sqlite_master SET sql = sqlite_rename_column(sql, type, name, %Q, %Q, %d, %Q, %d, 1) WHERE type IN ('trigger', 'view')
ROLLBACK TO changeset_apply
DELETE FROM %Q.'%q_docsize' WHERE docid = ?
ALTER TABLE %Q.'%q_segments' RENAME TO '%q_segments';
merge
MAX_DEFAULT_PAGE_SIZE=8192
invalid change: column %d - old.* value is %sdefined but new.* is %sdefined
cannot create %s trigger on view: %S
Auto logging environment variable set, but process is restricted. Ignoring.
DEFAULT_WAL_AUTOCHECKPOINT=1000
BEGIN EXCLUSIVE
checkpointed
SELECT*FROM\"%w\"
afpfs
BitOr
SqlExec
{}
offsets
carray
LAST TERM OF 
%!0.17g
ParseSchema
FLAGS parameter to json_valid() must be between 1 and 15
%s unfinalized statement: \"%s\"
ness
DEFAULT_AUTOVACUUM
%sc%d TEXT
RowSetTest
ResetSorter
\\u00
randomblob
);
THREADSAFE=2
IfNotZero
Copy
cache_size
[%lld]
cannot join using column %s - column not present in both tables
non-deterministic use of %s() in %s
docid
config
SAVEPOINT changeset
/*sort*/
view
fts5
SELECT rowid, rank FROM %Q.%Q ORDER BY %s(\"%w\"%s%s) %s
-wal
SeekGE
ResetCount
%s constraint failed
vtable constructor did not declare schema: %s
duplicate column name: %s
second argument to %#T() must be a constant between 0.0 and 1.0
USE TEMP B-TREE FOR %s(DISTINCT)
2026-04-09 12:25:13 8fa8248e303219400c646a885e36dfc52eae33d83f4412e3f369b2be5373aapl
DELETE FROM %Q.sqlite_master WHERE tbl_name=%Q and type!='trigger'
>
cannot drop %s column: \"%s\"
 WITHOUT ROWID
_parent
argument to %s() is not a valid SQL statement
strftime
ENABLE_FTS3_TOKENIZER
no tables specified
ENABLE_FTS5
PRAGMA journal_mode=DELETE
memdb(%p,%lld)
SQLITE_ACCEPTABLE_OVERALL_VM_STEP
NO ACTION
likely
acosh
%2d
tokenize
memvfs
unix
auto_vacuum=1
FkCheck
AUTOMATIC PARTIAL COVERING INDEX
sqlite_log
unknown tokenizer
deletemerge
readonly_shm
ro
Wrong number of columns for an rtree table
tables_used
 is never used
IMDPersistenceAgent
INSERT INTO %Q.%Q(%Q) VALUES('flush')
ENABLE_SQLLOG
trigger
UTF16be
%.3f
,%.*s INT
Multiply
p5
database
malformed JSON
sqlite_returning_%p
unopened
SETUP
start of 
block
data
COMMIT;\n
CursorHint
assetsd
sqlite_schema
trigger %T already exists
20e
0123456789ABCDEF0123456789abcdef
(subquery-%u)
temp_store_directory
desc
%r ORDER BY term does not match any column in the result set
trigram
SeekLT
p4
/*+%d bytes*/
foreign_key_list
ON
denying write to invalidated fd %d
BUG IN CLIENT OF libsqlite3.dylib: database integrity compromised by API violation: vnode %s while in use: %s
SQLITE_ACCEPTABLE_PAGES_PER_STEP
content
MUTEX_UNFAIR
uuid
ieee754_exponent
%c%u
VBegin
pragma_list
dflt_value
too many columns on %s
aes256
sqlite3
fts3_tokenizer
DELETE FROM %Q.'%q_segdir' WHERE level BETWEEN ? AND ?
DELETE FROM %Q.'%q_docsize' WHERE id=?
SQLite 
MobileSafari
cannot open value of type %s
percentile_cont
query aborted
malformed columnsize=... directive
CREATE TABLE x(key,value,type,atom,id,parent,fullkey,path,json HIDDEN,root HIDDEN)
BLOOM FILTER ON %S (
too many SQL variables
sqlite_detach
fts5: checksum mismatch for table \"%s\"
msdos
healthd
subqueries
_content
contentless_delete=1 is incompatible with columnsize=0
UPDATE \"%w\".\"%w_rowid\"SET 
(NULL)
unix-flock
error in %s %s after %s: %s
the NOT INDEXED clause is not allowed on UPDATE or DELETE statements within triggers
ENABLE_LOCKING_STYLE=1
0
avg
%s_%s.db
RC_XBS
NOT NULL
table %s may not be dropped
too many terms in compound SELECT
?,?,?
/dev/null
abbreviated query algorithm search
SCAN %S
abort due to ROLLBACK
x'
BUG IN CLIENT OF libsqlite3.dylib: illegal multi-threaded access to database connection
vacuum_%016llx
year
LZ4_RAW
\\n
denying shm read from invalidated fd %d
Checkpoint
addr
ANALYZE \"%w\".\"%w\"
cannot open virtual table: %s
full_column_names
sissii
unknown operation
reserve
current_timestamp
file is not a database
out of memory
IdxLE
pragma user_version = %d;\n
CREATE TRIGGER
%.18s-%s
glob
,%.*s
cannot open '%s' for reading
]
immutable
recon
UPDATE OR FAIL %Q.'%q_segdir' SET level=-1,idx=? WHERE level=? AND idx=?
_rowid
IFindKey
NewRowid
MemMax
lower
failed memory resize %u to %u bytes
Query: %s\n Execution Time: %llu ms\n
VACUUM \"%w\" INTO '%q'
Int64
datatype mismatch
ive
</b>
-journal
cannot open table without rowid: %s
cannot change %s wal mode from within a transaction
CHECK constraints
missing %s parameter in fts4 constructor
 FROM '%q'.'%q%s' AS x
unknown database %T
the \".\" operator
EXCEPT
Cannot add a column with non-constant default
rebuild
Compression method %ld not currently supported for operationType %ld
rtreenode
/Calendar/Calendar.sqlitedb
Null
%d %s\n
<unresolvable path>
SQLITE_FORCE_PROXY_LOCKING
GetSubtype
json
LIMIT
unsupported frame specification
SQLITE_ENABLE_VNODE_GUARDS
sqlite_source_id
,'%s',char(13))
invalid change: null value in PK
 NUM
subtype
sqlite_version
AND
DELETE FROM '%q'.'%q_idx' WHERE segid=?
16LE
IdxInsert
textkey
hex literal too big: %s%#T
virtual
table %S has %d columns but %d values were supplied
SQL logic error
,
Offset
orphan index
%s.xBestIndex malfunction
*** in database %s ***\n
INSERT INTO %Q.sqlite_master VALUES('trigger',%Q,%Q,0,'CREATE TRIGGER %q')
ENABLE_PREUPDATE_HOOK
IdxGT
see-
cannot create triggers on virtual tables
source and destination must be distinct
table schemas do not match
fchown
AggFinal
searchd
corrupt database
ON clause
    
unix-none
%s at line %d of [%.10s]
?
drop constraint
utf8
, T.l%d
CREATE TABlE vocab(term, doc, col, offset)
SCAN CONSTANT ROW
integrity-check
no such cursor: %lld
ion
select name,sql from sqlite_master where type = 'index' and rootpage != 0
Trace
Environment override of cache_size %d -> %d
data_version
%c?)
LIKE or GLOB pattern too complex
%04d
failed to set '%s' on truncated database %s, %d: %s\n
unknown database %s
-mj%06X9%02X
String8
Safety level may not be changed inside a transaction
idx IS CASE WHEN length(?4)=0 AND typeof(?4)='blob' THEN NULL ELSE ?4 END 
not authorized to use function: %#T
expressions prohibited in PRIMARY KEY and UNIQUE constraints
SELECT %s WHERE rowid = ?
SELECT pgno FROM '%q'.'%q_idx' WHERE segid=? AND term>? ORDER BY term ASC LIMIT 1
PRAGMA database_list
%.*s
vtab:%p
too many columns in %s
jsonb_replace
Delete
notused
database_list
no such index: %s
AFTER
sqlite3_open_v2 open failed with %d
ReopenIdx
%s %T already exists
In RTree %s.%s:\n%z
unixReplaceDatabase() failed with error %d for replacing '%s' with '%s' \n
TEXT
MobileNotes
view %s is circularly defined
SELECT %s FROM %s T WHERE T.%Q=?
Skipping vnode guard based on exemption path %s for file: %s
922337203685477580
internal query planner error
naturaleftouterightfullinnercross
VCheck
stat_get
nullif
asin
jsonb_array
unix-afp
SELECT * FROM %Q.sqlite_schema
ValueList
busy
no such column
remove_diacritics=1
malformed prefix=... directive
no such function: %s
entitlement \"%s\" or environment variable \"SQLITE_ENABLE_SEE=1\" required to activate SEE
cannot UPDATE generated column \"%s\"
unrecognized token: \"%s\"
SELECT NOT EXISTS(SELECT docid FROM %Q.'%q_content' WHERE rowid!=?)
SAVEPOINT fts3
InitCoroutine
DISTINCT
warning message
unrecognized matchinfo: %s
rtree_i32
open destination failed for %d\n
Replacement SPI only supports encrypted databases when keys match
Overriding cache_size %d -> %d
CREATE 
(null)
node
mem(%p,%lld)
queries_performance
Clear
 VIRTUAL TABLE INDEX 
Cannot add a PRIMARY KEY column
sqlite_rename_test
porter
, l%d
index_info
table_info
length
misuse
unix-posix
RowSetAdd
ifnull
stderr
%s is not supported for this process
sqlite_
GooglePhotos
unknown datatype for %s.%s: \"%s\"
rw
MATCH
tokendata
more than one 'header' parameter
tmpsqlitearchiveXXXXXX
misuse of aliased window function %s
not a writable directory
sqlite_attach
SELECT pgno FROM '%q'.'%q_idx' WHERE segid=? AND term<=? ORDER BY term DESC LIMIT 1
DELETE FROM %Q.'%q_content';
DIRECT_OVERFLOW_READ
COMMIT
SELECT name, type, sql FROM \"%w\".sqlite_schema WHERE sql NOT NULL AND type=='table' AND name!='sqlite_sequence'
suggestd
rtreedepth
IfNotOpen
geteuid
quick_check
atan
ed
SELECT nodeno FROM '%q'.'%q_rowid' WHERE rowid = ?1
ENABLE_BYTECODE_VTAB
ENABLE_MATH_FUNCTIONS
<Unknown>
AM
SELECT count(*) FROM %Q.'%q_segdir' WHERE level = ?
'rebuild' may not be used with a contentless fts5 table
ENABLE_DBSTAT_VTAB
lock_proxy_file
writable_schema
unable to identify the object to be reindexed
sin
compression_stream_init
fallocate
MaxPgcnt
vfs
SELECT size FROM %Q.'%q_docsize' WHERE docid=?
bl
SeekEnd
\"%w\"
ous
ENABLE_RTREE
auto_vacuum
Sequence
text
DELETE FROM %Q.'%q_docsize'
, c%d
changes
ENABLE_STMT_SCANSTATUS
foreign_keys
numeric
auto
REPLACE INTO %Q.'%q_segdir' VALUES(?,?,?,?,?,?)
SQLITE_AUTO_PROFILE
pipelined
wrong number of arguments to function highlight()
sqlite3changeset_apply(): no such table: %s
there is already another table or index with this name: %s
UPDATE \"%w\".sqlite_master SET sql = sqlite_drop_constraint(sql, %s) WHERE type='table' AND tbl_name=%Q COLLATE nocase
SELECT value FROM %Q.'%q_stat' WHERE id=?
Invalid argument to rtreedepth()
min
%s RETURNING is not available on virtual tables
parse error in tokenize directive
/
PRAGMA page_count
BEGIN DEFERRED; PRAGMA schema_version;
Blob
table %s may not be modified
u
 missing from index 
<b>...</b>
pragma auto_vacuum = %s;\n
pipe failed for %d\n
too many terms in ORDER BY clause
fts5: syntax error near \"%.1s\"
enci
tbl, ?2, stat
connections
foreign key mismatch - \"%w\" referencing \"%w\"
RTRIM
output file already exists
sqlite_stat?
50000
cannot create trigger on system table
flush
tmpsqlitereplacedbXXXXXX
CHECK
statement too long
NULL value in %s.%s
%.*s%s%s
notification message
%z%.*s
ENABLE_SNAPSHOT
AlipayWallet
DropTrigger
%s: %s.%s
%llu
anci
biliti
line %d: unterminated %c-quoted field\n
Found
SELECT*FROM\"%w\".%s ORDER BY rowid
Fragmentation of %u bytes reported as %u on page %u
SELECT sql FROM \"%w\".sqlite_schema WHERE type='index'
%s%s
unlikely
SELECT level, idx, end_block FROM %Q.'%q_segdir' WHERE level BETWEEN ? AND ? ORDER BY level DESC, idx ASC
DELETE FROM %Q.'%q_data';DELETE FROM %Q.'%q_idx';
read
Rtree depth out of range (%d)
sqllogFindAttached(): error in \"PRAGMA database_list\"
ORDER BY may not be used with non-aggregate %#T()
, 
unable to close due to unfinalized statements or unfinished backups
Param
malformed database schema (%s)
object name reserved for internal use: %s
percentile_disc
unable to delete/modify user-function due to active statements
%s: table does not support scanning
nsurlstoraged
function_list
am
T.%Q
SELECT length(data) FROM '%q'.'%q_node' WHERE nodeno = 1
pragma page_size = %d;\n
Program
rtrim
jsonb_remove
MAX_COMPOUND_SELECT=500
end
IMDPersistence
USING INDEX %s FOR IN-OPERATOR
-%T
sqlite_compileoption_used
illegal first argument to %s
SELECT %s%s FROM %Q.%Q WHERE (%s) IS (%s)
object
near \"%T\": syntax error
utf16be
integer overflow
database is locked
automerge=
unknown database: %s
VACUUM %s
opcode
true
circular reference: %s
BBB
CREATE TABLE ['\"]*
oid
frame ending offset must be a non-negative integer
SQLite format 3
null
NotNull
IntegrityCk
drop column
reverse_unordered_selects
multiple references to recursive table: %s
rows inserted
tbl_name='%q' AND type!='trigger'
automatic index on %s(%s)
%s/sqllog_%05d
no such savepoint: %s
cache_spill
on_update
inity
DELETE FROM %Q.sqlite_master WHERE name=%Q AND type='trigger'
fts5vocab: unknown table type: %Q
MAX_TRIGGER_DEPTH=1000
:auto:
vtable constructor failed: %s
textrekey
argument of ntile must be a positive integer
PRAGMA journal_mode=wal
Failed to open '%s' for read/write access (%s). Attemping to open as read-only
VFilter
NullRow
cannot release savepoint - SQL statements in progress
cloudd
incremental
if
pwrite64
dummy
NO
unable to use function %s in the requested context
SELECT data FROM %Q.'%q_node' WHERE nodeno=?
%s%.3x/
ln
segid, term, pgno, PRIMARY KEY(segid, term)
database table is locked: %s
ascii
HAVE_ISNAN
%s: %s.%s.%s
siX
write failed (%d)
MJ delete: %s
date
cannot UPSERT a view
sqlite_stat4
DEFAULT_MEMSTATUS=0
Unknown operation type %ld
pragma encoding
\\015
webdav
/Accounts/Accounts3.sqlite
OpenRead
SorterOpen
UPDATE \"%w\".sqlite_master SET sql = sqlite_add_constraint(sql, %.*Q, -1) WHERE type='table' AND tbl_name=%Q COLLATE nocase
PRAGMA main.cache_spill
unable to open database: %s
concat
group_concat
medialibraryd
foreign key on %s should reference only one column of table %T
row 
%s-journal
pragma journal_mode = %s;\n
FkIfZero
ignore_check_constraints
INTERSECT
json_quote
PRAGMA '%q'.table_xinfo('%q')
Once
collation_list
sqlite_autoindex_%s_%d
BUG IN CLIENT OF libsqlite3.dylib: database integrity compromised by API violation: vnode %s while in use
Last
ElseEq
-- 
ncol
LEFT-MOST SUBQUERY
octet_length
invalid database name \"%s\"
not an array element: %Q
misuse of aliased aggregate %s
index '%q'
failed to open temp database '%s' to reset truncated database %s with flags %x: %d\n
MakeRecord
AggInverse
sinh
Rewind
status
Cannot add a UNIQUE column
asinh
parse error in rank function: %s
SELECT parentnode FROM '%q'.'%q_parent' WHERE nodeno = ?1
B
iss
pinned
RELEASE changeset
Child page depth differs
%s.%z
cannot UPDATE
ptr
TypeCheck
sz=[0-9]*
to
%s clause should come after %s not before
UPDATE %Q.sqlite_master SET type='table', name=%Q, tbl_name=%Q, rootpage=0, sql=%Q WHERE rowid=#%d
pk
:memory:
iisX
50f-20a-20d
OpenDup
AggStep1
json_object() requires an even number of arguments
fts3
%lld %lld
contentless_delete
10000.0
Offset %u out of range %u..%u
VOpen
, ?
REPLACE INTO %Q.'%q_config' VALUES ('version', %d)
Too few columns for an rtree table
Gt
Freelist: 
inf
cannot use DEFAULT on a generated column
Add
bad JSON path: %Q
month
json_%s() needs an odd number of arguments
Not
NONE
json_valid
REPLACE INTO '%q'.'%q_data'(id, block) VALUES(?,?)
 FROM 
pread
wal_checkpoint
table %s may not be indexed
UPDATE OR FAIL %Q.'%q_segdir' SET level=? WHERE level=-1
 AND (?6 OR ?3 IS stat)
,%s%s%s
CreateBtree
FOREIGN KEY
cannot create INSTEAD OF trigger on table: %S
interrupted
ALTER TABLE %Q.'%q_segdir'   RENAME TO '%q_segdir';
fts5: corruption on page %d, segment %d, table \"%s\"
END;\n
NotFound
idx
day
reserved fts5 table name: %s
-1e999
narg
RAISE() may only be used within a trigger-program
iviti
ieee754(%lld,%d)
$
temporary storage cannot be changed from within a transaction
matchinfo
tokenchars=
%z, langid
no such tokenizer: %s
custom
__langid
Ne
ZeroOrNull
IdxRowid
%!.*f
FavoritesTodayWidget
CREATE TABLE \"%w\".\"%w_parent\"(nodeno INTEGER PRIMARY KEY,parentnode);
NotExists
callservicesd
\n)
pwrite
Transaction
ant
uuid_blob
tbl
flexnum
cannot create a TEMP index on non-TEMP table \"%s\"
json_array_length
bad schema: '%s' - %s
SequenceTest
SUBSTR_COMPATIBILITY
failed to set lock proxy file
SELECT 1 FROM temp.sqlite_master WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X' AND sql NOT LIKE 'create virtual%%' AND sqlite_rename_test(%Q, sql, type, name, 1, %Q, %d)=NULL 
corrupted
last write ended with return %ld expected %ld with errno %d\n
open
/dev/urandom
Subtract
%#T() may not be used as a window function
new
CREATE TABLE %Q.'%q_docsize'(docid INTEGER PRIMARY KEY, size BLOB);
/usr/tmp
row not in PRIMARY KEY order for %s
\"
ENABLE_UNKNOWN_SQL_FUNCTION
executing sql '%s' returned error %x with message:'%s'\n
%z, %Q HIDDEN, %s HIDDEN)
%lld
%s.lock
off
printf
open('%s') failed with errno %d
synchronous
name='%q' AND type='index'
like
frame specification
unistr
hashsize
er
Count
USE TEMP B-TREE FOR %s(ORDER BY)
columns
psow
instr
json_array_insert
bytecode
%s
jsonb_object
attempt to open \"%s\" as file descriptor %d
cannot INSERT into generated column \"%s\"
edit constraints of
%!0.15g
authorization denied
modeof
Cast
invalid arguments to fts4aux constructor
REPLACE INTO %Q.'%q_docsize' VALUES(?,?)
aliti
ALTER TABLE %Q.'%q_node'   RENAME TO \"%w_node\";ALTER TABLE %Q.'%q_parent' RENAME TO \"%w_parent\";ALTER TABLE %Q.'%q_rowid'  RENAME TO \"%w_rowid\";
INSERT INTO main.sqlite_stat1 VALUES(?1, CASE WHEN length(?2)=0 AND typeof(?2)='blob' THEN NULL ELSE ?2 END, ?3)
AND 
string or blob too big
Bad ptr map entry key=%u expected=(%u,%u) got=(%u,%u)
schema_version
conflicting ON CONFLICT clauses specified
column= value must be positive
pread('%s') failed returning %ld bytes with errno %d
PRAGMA schema_version
tanh
.\"
DELETE FROM %Q.'%q_segdir' WHERE level = ?
CREATE TABLE %Q.'%q_content'(%s)
, 1
indexed
json_each
unpinned
column index out of range
sqllogTraceDb(): database name too long (%d bytes)
CREATE TABLE %Q.sqlite_sequence(name,seq)
LEFT
Schema corrupt or not an rtree
%.4c%s%.16c
leaf
entitlement \"%s\" required to activate SEE
-
sqlite_drop_constraint
UTF-8
queries_persist
\"%w\" 
secure-delete
BUG_COMPATIBLE_20160819
16BE
%s %T cannot reference objects in database %s
frame starting offset must be a non-negative integer
sign
json_extract
error parsing prefix parameter: %s
foreign key
too many levels of trigger recursion
hidden
0x%x:%s
,origin
internal
fstat
ShiftLeft
issisii
sqlite\\_%
log2
json_error_position
SELECT 2 * total(1 + leaves_end_block - start_block)   FROM (SELECT * FROM %Q.'%q_segdir'         WHERE level = ? ORDER BY idx ASC LIMIT ?  )
aes128
isiX
denying fileSize on invalidated fd %d
DISTINCT is not supported for window functions
cannot add a STORED column
char
INSERT INTO 
user_version
json_tree
ANY(%s)
jsonb_group_object
INSERT OR REPLACE INTO '%q'.'%q_rowid' VALUES(?1, ?2)
DEFAULT_PAGE_SIZE=4096
pragma legacy_file_format = %d;\n
pragma_
strict
ORDER BY
ORDER BY clause
DELETE FROM '%q'.'%q_data' WHERE id>=? AND id<=?
iciti
UNIQUE constraint failed: %s.%s
issisi
view %s may not be altered
DROP TABLE '%q'.'%q_node';DROP TABLE '%q'.'%q_rowid';DROP TABLE '%q'.'%q_parent';
/PhotoData/Photos.sqlite
utf16le
DEFAULT_SECTOR_SIZE=4096
SELECT %s FROM \"%w\".\"%w\" WHERE NOT EXISTS (  SELECT 1 FROM \"%w\".\"%w\" WHERE %s)
0123456789abcdef
temporary trigger may not have qualified name
ENABLE_FTS3
SQLITE_SQLLOG_DIR
none
ROWID
CREATE%s INDEX %.*s
use DROP VIEW to delete view %s
UPDATE \"%w\".sqlite_master SET sql = sqlite_rename_column(sql, type, name, %Q, %Q, %d, %Q, %d, %d) WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X'  AND (type != 'index' OR tbl_name = %Q)
DELETE FROM %Q.'%q_docsize';
(FK)
LoadAnalysis
\n
fullfsync
<expr>
substring
database disk image is malformed
SELECT idx, start_block, leaves_end_block, end_block, root FROM %Q.'%q_segdir' WHERE level = ? AND idx = ?
fts5_insttoken
from
%s unfinished backup
exfat
SELECT*FROM\"%w\".%s WHERE %s ORDER BY rowid
index_list
Expire
ational
generated columns
virtual tables cannot use computed columns
no such trigger: %S
SQLITE_ENABLE_THREAD_ASSERTIONS
unknown special query: %.*s
sqllogCopydb(): error backing up database
IfSizeBetween
median
Function
BeginSubrtn
rename columns of
[]
@  
Lt
,schema HIDDEN
SELECT %s FROM %s T WHERE T.%Q >= ? AND T.%Q <= ? ORDER BY T.%Q ASC
SELECT parentnode FROM %Q.'%q_parent' WHERE nodeno=?1
SoftNull
QNaN
abs
json_object() labels must be TEXT
%Q, 
header
Pythonsqlite3
FIRST
Dimension %d of cell %d on node %lld is corrupt relative to parent
OMIT_AUTORESET
compression_stream_process
 REAL
atan2
SELECT max(level) FROM %Q.'%q_segdir' WHERE level BETWEEN ? AND ?
ieee754_mantissa
see-cccrypt
MAX_MMAP_SIZE=20971520
IdxLT
MobileMail
alli
ioctl
malformed locale=... directive
SELECT'INSERT INTO %s.'||quote(name)||' SELECT*FROM\"%w\".'||quote(name)FROM %s.sqlite_schema WHERE type='table'AND coalesce(rootpage,1)>0
ltrim
izer
trim
SELECT * FROM (SELECT 'sqlite_schema' AS name,1 AS rootpage,'table' AS type UNION ALL SELECT name,rootpage,type FROM \"%w\".sqlite_schema WHERE rootpage!=0)
sqlite_rename_column
json_group_array
max
PRAGMA writable_schema=OFF;\n
getcwd
journal_mode
PRAGMA table_info=%Q
CORRELATED 
SELECT %s WHERE rowid BETWEEN %lld AND %lld ORDER BY rowid %s
SELECT segid, term, (pgno>>1), (pgno&1) FROM %Q.'%q_idx' WHERE segid=%d ORDER BY 1, 2
\n;\n
create
UPDATE %Q.sqlite_master SET type='%s', name=%Q, tbl_name=%Q, rootpage=#%d, sql=%Q WHERE rowid=#%d
fts4
%!.15g
threads
sqrt
current_date
%02d:%02d
MAX_COLUMN=2000
more than one 'columns' parameter
SELECT*FROM\"%w\".\"%w\"
Auxiliary rtree columns must be last
%s_%05d.sql
r
tmpsqlitetruncatedbXXXXXX
.
recursive aggregate queries not supported
%d values for %d columns
s
SAVEPOINT replace_op
%s;\n
PRAGMA user_version
path error (len %d)
nolock
excluded
a NATURAL join may not have an ON or USING clause
DELETE FROM %Q.sqlite_master WHERE name=%Q AND type='index'
malformed detail=... directive
ieee754_to_int
IntCopy
Cannot add a REFERENCES column with non-NULL default value
datetime
Filter
dataaccessd
query_only
type
 UNIQUE
PRIMARY KEY
quote
DEFAULT_WORKER_THREADS=0
delete
recovered %d frames from WAL file %s
-9e999
USE TEMP B-TREE FOR %s
reset
ENABLE_SETLK_TIMEOUT
BEGIN
VIEW
FILTER clause may only be used with aggregate window functions
SELECT raise(ABORT,%Q) FROM \"%w\".\"%w\"
SELECT sqlite_fail('constraint failed', %d) FROM %Q.%Q AS x WHERE x.%.*s IS NULL
SELECT %s FROM %s AS T
fts5: syntax error near \"%.*s\"
UPDATE \"%w\".sqlite_master SET sql = sqlite_add_constraint(sqlite_drop_constraint(sql, %d), %.*Q, %d) WHERE type='table' AND tbl_name=%Q COLLATE nocase
SELECT sqlite_fail('constraint failed', %d) FROM %Q.%Q WHERE (%.*s) IS NOT TRUE
sqlite_find_constraint
ent
ieee754_from_blob
OpenEphemeral
busy_timeout
: 
);\n
logging
zeroblob(%d)
mod
sqlite_rename_table
API call with %s database connection pointer
multiple links to file: %s
btreeInitPage() returns error code %d
 EXISTS
seekAndWrite
schema
MERGE (%s)
rekey
parameters
random
DELETE FROM main.sqlite_stat1 WHERE tbl=?1 AND idx IS CASE WHEN length(?2)=0 AND typeof(?2)='blob' THEN NULL ELSE ?2 END AND (?4 OR stat IS ?3)
affected by unexpected operations
non-text filename
iif
the fraction argument to %%s() is not between 0.0 and %.1f
utc
%s a subset of columns on fts5 contentless-delete table: %s
ative
%s-wal
8
infinity
*]
Cannot add a column to a view
col
vnguard
TEXT value in %s.%s
/Library/AddressBook/AddressBook.sqlitedb
DEFAULT_JOURNAL_SIZE_LIMIT=32768
CREATE TABLE x(value INTEGER PRIMARY KEY)
\\r
/**** ERROR: (%d) %s *****/\n
MustBeInt
ResultRow
no such module: %s
insert
CREATE TABLE %Q.'%q_segdir'(level INTEGER,idx INTEGER,start_block INTEGER,leaves_end_block INTEGER,end_block INTEGER,root BLOB,PRIMARY KEY(level, idx));
*** 
no such table column: %s.%s
fchmod
DeferredSeek
no such index: %S
no such vfs: %s
unrecognized order: %s
RECURSIVE STEP
snippet
20c:20e
row
SELECT
ATTACH '%q' AS '%q'; -- clock=%d\n
Permutation
unrecognized token: \"%T\"
unknown function: %#T()
table-function argument
localtime
DELETE FROM '%q'.'%q_parent' WHERE nodeno = ?1
%s%.3x+%.6x
%Q
ieee754
Page %u: pointer map referenced
%s is %u but should be %u
ambiguous column name
access to view \"%s\" prohibited
RELEASE fts3
/****** %s ******/\n
INSERT INTO sqlite_schema(type,name,tbl_name,rootpage,sql)VALUES('table','%q','%q',0,'%q');
 %Q
<src path null>
UPDATE %Q.sqlite_master SET tbl_name = %Q, name = CASE WHEN type='table' THEN %Q WHEN name LIKE 'sqliteX_autoindex%%' ESCAPE 'X'      AND type='index' THEN 'sqlite_autoindex_' || %Q || substr(name,%d+18) ELSE name END WHERE tbl_name=%Q COLL
iissssss
40f
rmdir
char*
,%.*s REAL
mremap
frame starting offset must be a non-negative number
, T.%Q
case_sensitive
logi
entli
_node
mkdir
Failed to determine code signing flags
..%s
jsonb_array_insert
tne
LZFSE
fcntl(%d) failed: errno=%d\n
Tree %u page %u: 
UPDATE \"%w\".sqlite_master SET sql = printf('%%.%ds, ',sql) || %Q || substr(sql,1+length(printf('%%.%ds',sql))) WHERE type = 'table' AND name = %Q
<b>
w
k PRIMARY KEY, v
ENABLE_CARRAY
RELEASE replace_op
cannot fstat db file %s
cell_size_check
RESTRICT
INSERT INTO\"%w\".\"%w_rowid\"(rowid,nodeno)VALUES(?1,?2)ON CONFLICT(rowid)DO UPDATE SET nodeno=excluded.nodeno
linked
Jump
Compare
CREATE AUTOMATIC INDEX ON %s(
SELECT CASE WHEN quick_check GLOB 'CHECK*' THEN raise(ABORT,'CHECK constraint failed') WHEN quick_check GLOB 'non-* value in*' THEN raise(ABORT,'type mismatch on DEFAULT') ELSE raise(ABORT,'NOT NULL constraint failed') END  FROM pragma_quic
 IS ?
SELECT 
renamed
 is not a directory
spotlightknowledged.updater
AUTOINCREMENT is only allowed on an INTEGER PRIMARY KEY
;
at
rtree
unknown datatype: %Q
%z%s\"%w\".\"%w\".\"%w\"
INT
access
non-deterministic functions
json_insert
eed
Node %lld missing from database
Wrong number of entries in %%%s table - expected %lld, actual %lld
file-read-metadata
UTF-16
MAX_VDBE_OP=250000000
SELECT sqlite_fail('constraint %q already exists', %d) FROM \"%w\".sqlite_master WHERE type='table' AND tbl_name=%Q COLLATE nocase AND sqlite_find_constraint(sql, %Q)
Inf input to %%s()
%s_data
'delete-all' may only be used with a contentless or external content fts5 table
ATTACH
%
SQLITE_ACCEPTABLE_RATIO_VM_STEP_TO_STEP
(blob)
empty_result_callbacks
index expressions
index associated with UNIQUE or PRIMARY KEY constraint cannot be dropped
pi
ble
CursorLock
defer_foreign_keys
ceil
RELEASE changeset_apply
main
PRAGMA cache_size=%d
sqlite_stat%d
sqlite_stat3
CREATE TABLE x(
Too many columns for an rtree table
too many terms in %s BY clause
USING
atanh
%02d
routined
automerge
localhost
ENABLE_PERCENTILE
STMTJRNL_SPILL=131072
 VALUES(
PRAGMA integrity_check
:auto: (not held)
ColumnsUsed
BLOB
auto-index
close deferred due to
JournalMode
max rootpage (%u) disagrees with header (%u)
mode
failed to allocate %u bytes of memory
now
REPLACE INTO %Q.'%q_stat' VALUES(?,?)
SELECT %s,%s FROM \"%w\".\"%w\", \"%w\".\"%w\" WHERE %s AND (%z)
memdb
/* %s */ 
normal
UPDATE temp.sqlite_master SET sql = sqlite_rename_quotefix('temp', sql)WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X' AND sql NOT LIKE 'create virtual%%'
on
Eq
case_sensitive_like
UPDATE %Q.sqlite_master SET rootpage=%d WHERE #%d AND rootpage=#%d
SQLITE_ENABLE_LOGGING
user 'setup'(248) opening database '%s' with SQLITE_OPEN_READWRITE
fts5: %s queries are not supported (detail!=full)
ORDER BY without LIMIT on %s
pragma journal_mode
pragma encoding = %s;\n
aggregate
CREATE TABlE vocab(term, col, doc, cnt)
BEGIN IMMEDIATE; COMMIT;
count_changes
/Library/AddressBook/AddressBookImages.sqlitedb
MAX_ATTACHED=10
write
%.16g
database %s is already in use
homed
DELETE FROM %Q.'%q_segdir' WHERE level = ? AND idx = ?
%z%s%Q
{%lld
failed to break stale lock on %s, %s\n
index %s already exists
fts5: corruption in table \"%s\"
encoding
al
SELECT nodeno FROM %Q.'%q_rowid' WHERE rowid=?1
no such column: \"%s\"
smbfs
/Notes/notes.sqlite
integrity_check
no query solution
Index optimized
Node %lld is too small (%d bytes)
'%s'
invalid page number %u
parent
json_replace
ization
ation
denying sync of invalidated fd %d
duetexpert
,?
csv
file unlinked while open: %s
Concat
REAL
detail
there is already an index named %s
after rename
array_insert
\\u000b
prefix
docid INTEGER PRIMARY KEY
remove_diacritics
rtreecheck
MAX_LIKE_PATTERN_LENGTH=50000
format
string_agg
SorterCompare
OffsetLimit
truncate
40f-20a-20d
Failed to set vnode guard on %s (%d): %s
memory
UPSERT not implemented for virtual table \"%s\"
remove_diacritics=0
ENABLE_COLUMN_METADATA
locking_mode
hw.ncpu
ize
ROLLBACK TO fts3
%z: %s
SEARCH
second argument to nth_value must be a positive integer
SELECT 1 FROM \"%w\".sqlite_master WHERE name NOT LIKE 'sqliteX_%%' ESCAPE 'X' AND sql NOT LIKE 'create virtual%%' AND sqlite_rename_test(%Q, sql, type, name, %d, %Q, %d)=NULL 
tan
unable to close due to
%z,?%d
fts5_locale() requires locale=1
ieee754_inc
RANGE with offset PRECEDING/FOLLOWING requires one ORDER BY expression
SET NULL
UPDATE sqlite_temp_schema SET sql = sqlite_rename_table(%Q, type, name, sql, %Q, %Q, 1), tbl_name = CASE WHEN tbl_name=%Q COLLATE nocase AND   sqlite_rename_test(%Q, sql, type, name, 1, 'after rename', 0) THEN %Q ELSE tbl_name END WHERE typ
duplicate WITH table name: %s
iveness
PRAGMA foreign_keys=OFF;\nBEGIN TRANSACTION;\n
break
fts5_get_locale
fulness
sz
cannot open table with generated columns: %s
Close
double
DELETE FROM %Q.sqlite_sequence WHERE name=%Q
_rowid_
ENABLE_FTS4
AggValue
no such index: \"%s\"
file:
cannot %s %s \"%s\"
REPLACE INTO %Q.'%q_content' VALUES(%s)
sql_read_archive_header('%s') failed with errno %d
NULL
ufs
partial
no such function: %#T
no such window: %s
ambiguous reference to %s in USING()
-- TRIGGER %s
SQLite ARCHIVE_APPLE_1
sql_error
Savepoint
=%Q
unknown column \"%s\" in foreign key definition
CREATE TABLE x(term, col, documents, occurrences, languageid HIDDEN)
pcx
malformed tokendata=... directive
%.*s%s
current_time
(
stat
Move
Expression tree is too large (maximum depth %d)
%d:%s
DELETE FROM %Q.'%q_stat'
DecrJumpZero
%!S
GROUP BY
unhex
DELETE FROM %Q.'%q_content' WHERE id=?
) VALUES(?
truncated
error in %s %s%s%s: %s
REPLACE INTO %Q.'%q_config' VALUES(?,?)
INSERT INTO '%q'.'%q_idx'(segid,term,pgno) VALUES(?,?,?)
%z%s%z
CREATE TABLE x(addr INT,opcode TEXT,p1 INT,p2 INT,p3 INT,p4 TEXT,p5 INT,comment TEXT,subprog TEXT,nexec INT,ncycle INT,stmt HIDDEN);
bad parameter: '%s'
un
cannot open file
%d
there is already a table named %s
RIGHT-JOIN %s
carray-bind
VInitIn
unsupported use of NULLS %s
free space corruption
9e999
misuse of aggregate: %#T()
column%d
>? AND %s
SELECT coalesce((SELECT max(blockid) FROM %Q.'%q_segments') + 1, 1)
);CREATE TABLE \"%w\".\"%w_node\"(nodeno INTEGER PRIMARY KEY,data);
ENABLE_UPDATE_DELETE_LIMIT
com.apple.libsqlite3.telemetry
OpenWrite
invalid rootpage
keybagd
error in generated column \"%s\"
typeof
jsonb_extract
SET DEFAULT
drop column from
, x.'%q'
lstat
SorterInsert
Pagecount
too many arguments on function %T
the fraction argument to %%s() is not the same for all input rows
syslog
NUMERIC value in %s.%s
UPDATE %Q.'%q_segdir' SET idx = ? WHERE level=? AND idx=?
CREATE TABLE x(%s %Q HIDDEN, docid HIDDEN, %Q HIDDEN)
Dimension %d of cell %d on node %lld is corrupt
unix-proxy
IsNull
no such view
unknown table option: %.*s
misuse of aggregate: %s()
flags must include SQLITE_OPEN_READONLY or SQLITE_OPEN_READWRITE
/AddressBook/AddressBook.sqlitedb
malformed MATCH expression: [%s]
_ROWID_
cannot modify %s because it is a view
Sqlite_Heap_homed
database table is locked
MAX_SQL_LENGTH=1000000000
notnull
CHECK constraint failed in %s
usermerge
constraint may not be dropped: %s
fts3cursor
overflow
'
default_cache_size
delete-all
recursive definition for %s.%s
dbstat
match
authorizer malfunction
RELEASE
last_insert_rowid
cosh
%c%04d-%02d-%02d %02d:%02d:%06.3f
decompressor
i16@?0^{sqlite3_stmt=}8
And
SetCookie
bird
recursive_triggers
table %s may not be altered
INSERT INTO %Q.'%q_content' VALUES(%s)
sql dump
nfs
SELECTs to the left and right of %s do not have the same number of result columns
noop
CREATE TABLE %Q.'%q_segments'(blockid INTEGER PRIMARY KEY, block BLOB);
SYSTEM_MALLOC
pragma auto_vacuum
cannot open %s column for writing
pread64
index_xinfo
Replace database failed because TMPDIR is not set correctly\n
AddImm
DELETE
input to %%s() is not numeric
highlight
 WHERE rowid=?1
uuid_str
Source file '%s' is not an SQLite database file or backup archive, or is encrypted.  Type is %d
rename failed (%d)
recovered %d pages from %s
IsType
IfEmpty
analysis_limit
hexrekey
jsonb_each
overflow list length
%s: \"%s\" - should this be a string literal in single-quotes?
default value of column [%s] is not constant
trigger \"%s\" may not write to shadow table \"%s\"
table %S has no column named %s
time
no more rows available
unable to delete/modify collation sequence due to active statements
 (
power
unrecognized column option: %s
DEFAULT_WAL_SYNCHRONOUS=1
CREATE TABLE IF NOT EXISTS 
com.apple.private.sqlite.sqlite-encryption
munmap
denying fcntl on invalidated fd %d
misuse of %s function %#T()
expected %d columns for '%s' but got %d
unknown join type: %T%s%T%s%T
%Q%s
SetStoreUpdateService
flgs
triggers nested too deep
uncompress
ALTER TABLE %Q.'%q_docsize'  RENAME TO '%q_docsize';
%_parent
%z%s\"%w\".\"%w\".\"%w\"=\"%w\".\"%w\".\"%w\"
%z%s\"%w\".\"%w\".\"%w\" IS NOT \"%w\".\"%w\".\"%w\"
denying read from invalidated fd %d
%!.*g
UTF16
Too many entries in SQLITE_EXEMPT_PATH_FROM_VNODE_GUARDS, truncating list to first %d entries
/tmp
jsonb
more than one '%s' parameter
a JOIN clause is required before %s
DELETE FROM %Q.'%q_content' WHERE rowid = ?
SAVEPOINT changeset_apply
invalid change: defined value in PK of new.* record
%r %s BY term out of range - should be between 1 and %d
DELETE FROM %Q.%s WHERE %s=%Q
ReleaseReg
%s prohibited in %s
 INT
%s unfinalized statement
separators
DELETE FROM '%q'.'%q_node' WHERE nodeno = ?1
DEFAULT_RECURSIVE_TRIGGERS
temporary
Goto
If
unsupported file format
virtual tables may not be indexed
total
ASC
ical
;\n
SELECT sql FROM \"%w\".sqlite_schema WHERE type='table'AND name<>'sqlite_sequence' AND coalesce(rootpage,1)>0
 %g
TraceSQL(%p): %s\n
grindrx
Vacuum
TableLock
Recursion limit
json_type
bad parameter or other API misuse
SELECT sz%s FROM %Q.'%q_docsize' WHERE id=?
com.apple.sqlite
%s. See syslog for more information
freelist leaf count too big on page %u
a
CASCADE
DEFAULT_MMAP_SIZE=0
MALLOC_SOFT_LIMIT=1024
denying truncate of invalidated fd %d
SeekHit
RowCell
incremental_vacuum
\\u0000
old
coalesce
unsafe use of virtual table \"%s\"
pragma user_version
stat failed for %d\n
apfs
ERROR: sqlite database is locked because it is in use by another host that holds a host-exclusive lock on %s; this host (UUID %s) cannot override the host-exclusive lock until the other host (UUID %s) releases its locks on %s\n
fsync
CREATE BLOOM FILTER
pow
SQLITE_MALLOC_ZONE
%s-shm
Return
Integer
SorterData
attached databases must use the same text encoding as main database
%.*s %s%s
, x.%Q
fts5: missing row %lld from content table %s
pragma application_id
invalidated open fd: %d (0x%02lx)
ShiftRight
coll
fts3_tokenizer requires bound parameters
no such fts5 table: %s.%s
 AND (?%d OR ?%d IS %w.%w)
number of columns in foreign key does not match the number of columns in the referenced table
UTF-16le
iz
freeonclose
Or
itunesstored
p3
%d columns assigned %d values
invalid Unicode escape
subsec
json_set
RowSetRead
c
shared
PM
%Q.'%q_%s'
insttoken
no such table: 
SQLITE_MIN_CACHE_SIZE
temp_store
%s.%s
RIGHT
SCAN
UPDATE \"%w\".sqlite_master SET sql = sqlite_rename_table(%Q, type, name, sql, %Q, %Q, %d) WHERE (type!='index' OR tbl_name=%Q COLLATE nocase)AND   name NOT LIKE 'sqliteX_%%' ESCAPE 'X'
ate
)
openDirectory
<
unknown tokenizer: %s
unrecognized option: \"%.*s\"
unable to get the page. error code=%d
add column
%02x
 SET 
sandbox_check
exclusive
BEGIN EXCLUSIVE;\nCOMMIT;\n
Paper
SorterNext
compile_options
window
corrupt schema
remove_diacritics=2
SELECT 1 FROM %Q.'%q_segments' WHERE blockid=? AND block IS NULL
IntelligencePlatformComputeService
FilterAdd
qualified table names are not allowed on INSERT, UPDATE, and DELETE statements within triggers
replace(
%s: %s
 LEFT-JOIN
SELECT * FROM %Q.%Q
sqlite3changeset_apply(): table %s has %d columns, expected %d or more
%Q.
hfs
sqliteplocks
PRAGMA main.cache_size
Destroy
INSERT OR REPLACE INTO '%q'.'%q_parent' VALUES(?1, ?2)
DEFAULT_LOOKASIDE=1200,40
200
REUSE SUBQUERY %d
Invalid parameter to environment variable SQLITE_MALLOC_ZONE: \"%s\". Supported values are \"default\" and \"custom\"\n
wrong number of arguments to function snippet()
ALTER TABLE %Q.'%q_stat'  RENAME TO '%q_stat';
USE_URI
ZLIB
Halt
VCreate
cannot open savepoint - SQL statements in progress
multiple recursive references: %s
PRAGMA 
/var/tmp
legacy_alter_table
unable to validate the inverted index for FTS5 table %s.%s: %s
SELECT count(*) FROM %Q.'%q%s'
irb
CO-ROUTINE %!S
String
ORDER
cannot create triggers on shadow tables
expected integer, got \"%.*s\"
compression_stream_destroy
getpagesize
 USING INTEGER PRIMARY KEY (%s
more than %d aggregate terms
stat_init
acos
%s contentless fts5 table: %s
INSERT INTO %s.sqlite_schema SELECT*FROM \"%w\".sqlite_schema WHERE type IN('view','trigger') OR(type='table'AND rootpage=0)
comment
Prev
%s %S%s
unixepoch
unknown error
multiple content_rowid=... directives
SELECT 1 FROM sqlite_master LIMIT 1
S
CREATE VIRTUAL TABLE %T
json_object
MAX_VARIABLE_NUMBER=500000
SCopy
VRename
missing datatype for %s.%s
AUTOMATIC COVERING INDEX
sqlite_altertab_%s
LZ4
page_count
categories
no such table: %s.%s
close
no such table
.%.*s
id INTEGER PRIMARY KEY, block BLOB
INSERT OR REPLACE INTO '%q'.'%q_node' VALUES(?1, ?2)
INTEGER
biomesyncd
MATERIALIZE %!S
ance
ou
mmap_size
stat_push
substr
SELECT ? UNION SELECT level / (1024 * ?) FROM %Q.'%q_segdir'
contentless_unindexed=1 requires a contentless table
ALTER TABLE %Q.'%q_%s' RENAME TO '%q_%s';
PRAGMA synchronous = 0
OpenPseudo
IN(...) element has %d term%s - expected %d
%s_segments
no
Variable
Multiple uses for byte %u of page %u
checkpoint_fullfsync
%s in \"%s\"
 USING COVERING INDEX 
ful
ROLLBACK; -- due to errors\n
temp
seqno
type='trigger' AND name='%q'
PRAGMA table_list
CREATE TABLE IF NOT EXISTS %Q.'%q_stat'(id INTEGER PRIMARY KEY, value BLOB);
PureFunc
database is already attached
Invalid key value
set
%_rowid
,'%s',char(10))
Truncate database failed because TMPDIR is not set correctly\n
PRAGMA journal_mode=WAL
ClrSubtype
\n  
(%s%u)
BitAnd
.\"%.*s\"
50f
unordered*
hght
SELECT idx, start_block, leaves_end_block, end_block, root FROM %Q.'%q_segdir' WHERE level = ? ORDER BY idx ASC
ic
Source file '%s' is not an SQLite database file, or is encrypted.  Type is %d
incremental_vacuum enabled with a max rootpage of zero
too many FROM clause terms, max: %d
%06.3f
Sqlite_Heap
CCCRYPT256
subrtnsig:%d,%s
SorterSort
HaltIfNull
Abortable
sqlite_stat1
 of index 
expr_implies_expr
ALTER TABLE %Q.'%q_content'  RENAME TO '%q_content';
unix-excl
cannot commit - no transaction is active
table_list
ieee754_from_int
syntax error
create failed (%d)
SQLITE_TMPDIR
no such rowid: %lld
likelihood
 AND 
cannot use RETURNING in a trigger
version
BEGIN DEFERRED; PRAGMA schema_version
*
invalid fts5 file format (found %d, expected %d or %d) - run 'rebuild'
ement
invalid uri authority: %.*s
sqlite_compileoption_get
julianday
pragma legacy_file_format
%s/etilqs_%llx%c
generated column loop on \"%s\"
cannot drop column \"%s\": no other columns exist
CREATE TABLE %Q.'%q_%q'(%s)%s
siriknowledged
COMPILER=clang-21.0.0
undefined
-conch
jsonb_set
cannot rollback - no transaction is active
false
restart
a generated column
access permission denied
EndCoroutine
NOCASE
no such %s mode: %s
%Q.%Q
alism
while executing statement ('%s') it failed with error code %d and reason:'%s'\n
replace
WHERE name=%Q
sqlite_temp_master
page_size
yes
%r 
sqlite_add_constraint
->
languageid
parse error in \"%s\"
DELETE FROM sqlite_sequence;\n
SCAN %s%s%s
,a%d
SeekRowid
index %s stores an imprecise floating-point value for row 
logging-persist
program
VNext
automatic_index
fts5: corruption found reading blob %lld from table \"%s\"
sqllogFindFile(): error in fopen()
optimize
attempt to write a readonly database
L* N* Co
able
stmt-pointer
cannot open view: %s
biomed
UNION ALL
 WHERE 
table_xinfo
file
docsize
views may not be indexed
open flag(s) 0x%08x are reserved for VFS use and do not affect behaviour when passed to sqlite3_open_v2
ENABLE_API_ARMOR
statement aborts at 
wrong number of arguments to function %#T()
table \"%s\" has more than one primary key
jsonb_patch
,%s(?)
DEFAULT_FILE_FORMAT=4
PRAGMA defer_foreign_keys = 1
unixTruncateDatabase() failed with %d for replacing '%s' with flags %x\n
Ge
IfPos
read_uncommitted
OMIT_LOAD_EXTENSION
SeekGT
%z - %s
\"\\/bfnrt
partial index WHERE clauses
recursively defined fts5 content table
PARTITION clause
com.apple.private.sqlite.defensive
Failed to confine fd %d for file %s (%d): %s
SELECT %s ORDER BY rowid %s
fts5: column queries are not supported (detail=none)
NaN
%s,%u,%u,0x%llx,0x%llx,0x%llx,%lu,0x%llx,%s\n
INSERT INTO %Q.sqlite_master VALUES('index',%Q,%Q,#%d,%Q);
DROP TABLE IF EXISTS %Q.'%q_content';
ANALYZE sqlite_schema;\n
UNION
expr_compare
unrecognized matchinfo request: %c
fts5_api_ptr
 ORDER BY name
CollSeq
unique
exp
ieee754_to_blob
TMPDIR
copyfile returned unsuccessfully without setting errno, assuming target path was inaccessible
a%d=?%d
sqllogFindFile(): error reading index file
CREATE VIRTUAL TABLE temp.%Q USING %Q
unlink
YES
FkCounter
the INDEXED BY clause is not allowed on UPDATE or DELETE statements within triggers
private
merge=
DELETE FROM '%q'.'%q_idx' WHERE (segid, (pgno/2)) = (?1, ?2)
persist
row value misused
Node %lld is too small for cell count of %d (%d bytes)
cannot start a transaction within a transaction
%c\"%s\"
%.*z:%u
onoffalseyestruextrafull
fts5: parser stack overflow
%s\"%w\" TEXT
unixShmMap-stat
blob
not an error
PRAGMA %Q.page_size
CREATE TABlE vocab(term, doc, cnt)
DEFAULT_PCACHE_INITSZ=20
xctest
SeekLE
USE TEMP B-TREE FOR %sORDER BY
SELECT name, type, sql FROM \"%w\".sqlite_schema WHERE tbl_name=%Q COLLATE nocase AND type=='table'  AND sql NOT NULL
wrong number of arguments to function fts5_get_locale()
unlinked
-mj
 
bli
ENABLE_NORMALIZE
/usr/lib/libcompression.dylib
CREATE TABLE x(%.*s INT
CREATE TABLE 
unrecognized parameter: %s
IdxDelete
upper
ism
\\012
revoked
pragma journal_mode=wal
generated
MULTI-INDEX OR
timediff
SELECT max( level %% 1024 ) FROM %Q.'%q_segdir'
wrong number of vtable arguments
statfs
not authorized
AUTOINCREMENT not allowed on WITHOUT ROWID tables
jsonb_insert
json_patch
Extends off end of page
,arg HIDDEN
contentless_unindexed
rtree constraint failed: %s.(%s<=%s)
CODEC=see-cccrypt
%s;\n%s
Set a breakpoint in sqlite3MutexMisuseAssert to debug
affected by unexpected operation
unknown
ment
VACUUM
sqlite_sequence
This version of the encryption extension does not support an activation passphrase
MJ collide: %s
Init
Noop
parameters are not allowed in views
an index
com.apple.libsqlite3
fkid
log
must have at least one non-generated column
FTS expression tree is too large (maximum depth %d)
Index already optimal
multiple content=... directives
DROP TABLE IF EXISTS %Q.'%q_docsize';
SELECT name, type, sql FROM \"%w\".sqlite_schema WHERE name=='sqlite_sequence'
'%.*q'
ENABLE_FTS3_PARENTHESIS
 OR 
UPDATE main.
SELECT sql FROM \"%w\".sqlite_schema WHERE sql NOT NULL  AND type IN ('index','trigger','view')  AND tbl_name=%Q COLLATE nocase
destination database is in use
testfixture
\\\"
DEFAULT_CACHE_SIZE=128
PRAGMA defer_foreign_keys = 0
rb
line %d: unescaped %c character
F_GETLKPID undefined or not supported, _sqlite3_lockstate falling back to F_GETLK
TABLE
SELECT * FROM %Q.'%q_rowid'
NUM
sum
unable to validate the inverted index for FTS%d table %s.%s: %s
SELECT 1 FROM pragma_index_list(%Q) WHERE origin='pk'
DISTINCT aggregates must have exactly one argument
BEFORE
iti
FinishSeek
out of
%s.rowid
round
unable to open database file
order
MAX_PAGE_COUNT=1073741823
N.
unsupported encoding: %s
%s)%s
INDEX %d
NOT
temporary table name must be unqualified
ContactsCoreSpotlightExtension
-- Main database is '%q'\n
Gosub
DROP INDEX IF EXISTS \"%w\"
module_list
non-integer argument passed to function fts5_get_locale()
database corruption
MAX_FUNCTION_ARG=127
BitNot
id
OID
invalid
SELECT idx FROM %Q.'%q_segdir' WHERE level=? ORDER BY 1 ASC
Page %u: never used
 TEXT
SELECT stat FROM %Q.sqlite_stat1 WHERE tbl = '%q_rowid'
SQLITE_SQLLOG_REUSE_FILES
subsecond
json_remove
id INTEGER PRIMARY KEY, sz BLOB, origin INTEGER
cannot DELETE from contentless fts5 table: %s
jsonb_tree
DEFAULT_SYNCHRONOUS=2
sqlite3changeset_apply(): primary key mismatch for table %s
ReadCookie
Remainder
incomplete input
DROP TABLE IF EXISTS %Q.'%q_data';DROP TABLE IF EXISTS %Q.'%q_idx';DROP TABLE IF EXISTS %Q.'%q_config';
ing
no such collation sequence: %s
all VALUES must have the same number of terms
SELECT (SELECT max(idx) FROM %Q.'%q_segdir' WHERE level = ?) + 1
DELETE FROM %Q.'%q_segments' WHERE blockid BETWEEN ? AND ?
CREATE TABLE x(input, token, start, end, position)
error in tokenizer constructor
ousness
+- \n\t0123456789
key
ROLLBACK
hybridsearchd
SeekScan
full
Cannot add a NOT NULL column with default value NULL
%z%Q, 
eli
DELETE FROM '%q'.'%q_rowid' WHERE rowid = ?1
%s; -- clock=%d\n
tbl,idx,stat
--
CREATE TABLE x(type TEXT,schema TEXT,name TEXT,wr INT,subprog TEXT,stmt HIDDEN);
wal
truncate failed on '%s' with errno %d\n
activate_extensions
struct iovec
json_array
2nd reference to page %u
%s references tables to its right
INDEX %s
into
Failed to read ptrmap key=%u
JSON nested too deep
sub-select returns %d columns - expected %d
LAST
DQS=3
explain
API called with NULL prepared statement
non-%s value in %s.%s
DELETE FROM %Q.'%q_segments'
INSERT INTO \"%w\".\"%w_node\"VALUES(1,zeroblob(%d))
Explain
implies_nonnull_row
disk I/O error
id INTEGER PRIMARY KEY
API called with finalized prepared statement
rowid not at end-of-record for row 
separators=
DropIndex
SCAN %d CONSTANT ROW%s
virtual tables may not be altered
SELECT t.%Q FROM %Q.%Q AS t WHERE t.%Q MATCH '*id'
0x
DELETE FROM %Q.'%q_content'
os_unix.c:%d: (%d) %s(%s) - %s
\t Attempted temporary directory at path '%s' with stat() errno %d and access errno %d%s\n
VUpdate
database schema is locked: %s
PRIMARY KEY missing on table %s
fast
enc
ORDER BY without LIMIT on UPDATE
sqlite_drop_column
REPLACE INTO %Q.'%q_segments'(blockid, block) VALUES(?, ?)
VDestroy
resentsd
COMPOUND QUERY
 %llu
ible
DEFAULT_CKPTFULLFSYNC
unix-nfs
broke stale lock on %s\n
COVERING INDEX %s
tokenchars
1e999
no such table: %s
full_fsync
cannot store %s value in %s column %s.%s
soft_heap_limit
SELECT level, count(*) AS cnt FROM %Q.'%q_segdir'   GROUP BY level HAVING cnt>=?  ORDER BY (level %% 1024) ASC, 2 DESC LIMIT 1
volume does not support data protection, stripping SQLITE_OPEN_FILEPROTECTION_* flags
UNIQUE
p2
trusted_schema
SQLITE_AUTO_TRACE
v8@?0
mmap
perl
syntax error after column name \"%.*s\"
%d %d %d %d 
hard_heap_limit
VIEWs and/or subqueries nested too deep
cannot override %s of window: %s
20b:20e
fts5_source_id
SELECT count(*) FROM %Q.'%q_%s'
fts5: 2026-04-09 12:25:13 8fa8248e303219400c646a885e36dfc52eae33d83f4412e3f369b2be53737732
IncrVacuum
Affinity
too many columns in result set
UPDATE \"%w\".sqlite_master SET sql = sqlite_drop_column(%d, sql, %d) WHERE (type=='table' AND tbl_name=%Q COLLATE nocase)
40f-21a-21d
SELECT 0, 'tbl',  '', 0, '', 1, 0     UNION ALL SELECT 1, 'idx',  '', 0, '', 2, 0     UNION ALL SELECT 2, 'stat', '', 0, '', 0, 0
compression_stream_init failed for %d\n
PRAGMA writable_schema=ON;\n
statement aborts at %d: %s; [%s%s]
%sLIST SUBQUERY %d
rows updated
jsonb_group_array
unicode61
fts5_locale
IfNoHope
AggStep
database schema has changed
too many attached databases - max %d
SELECT idx, start_block, leaves_end_block, end_block, root FROM %Q.'%q_segdir' WHERE level BETWEEN ? AND ?ORDER BY level DESC, idx ASC
SELECT %s
unterminated string
Rowid
SELECT tbl,idx,stat FROM %Q.sqlite_stat1
on_delete
unixWrite
Tree %u page %u right child: 
cid
frame ending offset must be a non-negative number
is
database or disk is full
PRAGMA main.journal_mode
%s(%d)
Column
%u-ROW VALUES CLAUSE
SQLITE_ENABLE_SEE
%sON CONFLICT clause does not match any PRIMARY KEY or UNIQUE constraint
wrong number of arguments to function rtreecheck()
_rowid_, *
ATTACH x AS %Q
PRAGMA cache_spill=%d
9.0e999
table %s has %d values for %d columns
%s cannot use variables
sssiii
total_changes
default
CREATE TABLE x(type text,name text,tbl_name text,rootpage int,sql text)
unable to open a temporary database file for storing temporary tables
constraint failed
UPDATE %Q.'%q_segdir' SET start_block = ?, root = ?WHERE level = ? AND idx = ?
%z%s?%d
crisismerge
MAX_WORKER_THREADS=8
noskipscan*
close
startTime=%{signpost.description:begin_time}llu path=%s
%s
seekAndWrite(%lld, %d): improbable offset+len for file with size hint %lld
startTime=%{signpost.description:begin_time}llu db=%{public}p query=%{public,signpost.telemetry:string1,name=query}s
cache_spill
user 'setup'(248) opening database with SQLITE_OPEN_READWRITE
locking protocol: lockstate:%d, bShmUnreliable:%d, readOnly:%d
%d automatic index rows in [%s]
spilled %d pages during execution of [%s]
enableTelemetry=%s nSpill=%{public,signpost.telemetry:number1,name=rc}d writes=%{public,public,signpost.telemetry:number2}d
Error: %{errorMessage,public}s coalition: %{coalition,public}s database: %{database,public}s query: %{query,public}s
unable to close due to unfinalized statements or unfinished backups
rc=%{public}d db=%{public}p errMsg=%{public}s
execute
Error: %{errorMessage,public}s coalition: %{coalition,public}s
open
seekAndWrite(%lld, %d): improbable offset+len for file with observed size %lld
libsqlite: Error: Failed WAL locking protocol.
flagged inefficient query yielding %d results (expected vdbe steps ≤ %d, actual: %d) [%s]
enableTelemetry=%s rc=%{public,signpost.telemetry:number1,name=rc}d runCount=%{public}d nScan=%{public}d nAutoindex=%{public}d nSort=%{public}d nSpill=%{public}d nStep=%{public}d errMsg=%{public}s nVmStep=%{public,signpost.telemetry:number2
xRekey overwriting %{public}s page at index %d
Query: %s\n Execution Time: %llu ms\n
Failed to open temporary file at path %s: %s
sort without index in [%s]
_CS_DARWIN_USER_TEMP_DIR was deleted out from underneath this process. This is illegal and likely to cause crashes and data corruption.
SQL Error
startTime=%{signpost.description:begin_time}llu db=%p
TraceSQL(%p): %s\n
No temporary directory is accessible.  This is not a legitimate configuration.  Either the process environment or its sandbox is misconfigured.  Various library routines will error out abruptly.
pcache replacing page with non-zero refcount
%d scan steps for %d row steps in [%s]
```
