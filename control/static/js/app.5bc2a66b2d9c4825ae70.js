webpackJsonp([1],{NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n("7+uW"),o={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]};var r=n("VU/8")({name:"App"},o,!1,function(t){n("o8nZ")},null,null).exports,i=n("/ocq"),s=n("mvHQ"),l=n.n(s),u=n("//Fk"),c=n.n(u),m=n("mtWM"),d=n.n(m),f=n("zL8q"),b=n.n(f),p=n("M4fF"),v=void 0,h=0;function g(){a.default.nextTick(function(){h--,0===(h=Math.max(h,0))&&v&&_()})}var _=n.n(p).a.debounce(function(){v.close(),v=null},300),w=d.a.create({baseURL:"http://weebot.wisight.cn:28099/",timeout:2e4});w.interceptors.request.use(function(t){var e;return/get/i.test(t.method)&&(t.params=t.params||{}),(e=document.querySelector("body"))&&(0!==h||v||(v=f.Loading.service({target:e,text:"拼命加载中...",background:"rgba(0,0,0,0.3)"})),h++),t},function(t){return g(),c.a.reject(t)}),w.interceptors.response.use(function(t){g();var e=t.data;return console.log(e),200==e.status?e:(f.Message.error(e.errmsg),c.a.reject())},function(t){return g(),f.Message.error("请求失败"),c.a.reject(t)});var x=w;var y={data:function(){return{form:{model_number:"",is_usable:"",version:"",sn_number:""},formLabelWidth:"120px",dialogFormVisible:!1,tableData:[],page:1,size:10,total:1e3}},mounted:function(){this.getList()},methods:{currentChange:function(t){this.page=t,this.getList()},add:function(){var t,e=this;x({url:"admin/add",method:"post",data:t}).then(function(t){e.$message({type:"success",message:"新增成功!"}),e.getList()})},getList:function(){var t,e=this,n=this.page,a=this.size;(t={page:n,size:a},x({url:"admin/",method:"get",params:t})).then(function(t){e.tableData=t.data_list,e.total=t.total})},del:function(t){var e=this;this.$confirm("此操作将永久删除该数据, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){var n;(n={mobileuser_id:t},x({url:"admin/delete",method:"get",params:n})).then(function(t){e.$message({type:"success",message:"删除成功!"}),e.getList()})}).catch(function(){e.$message({type:"info",message:"已取消删除"})})},edit:function(t){this.form=JSON.parse(l()(t)),this.dialogFormVisible=!0},editSubmit:function(){var t=this,e=JSON.parse(l()(this.form));e.is_usable=e.is_usable?1:0,delete e.create_time,function(t){return x({url:"admin/update",method:"post",data:t})}(e).then(function(e){t.dialogFormVisible=!1,t.$message({type:"success",message:"修改成功!"}),t.getList()})}}},k={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"index"},[n("el-button",{staticStyle:{"margin-bottom":"10px"},attrs:{type:"primary"},on:{click:t.add}},[t._v("新增")]),t._v(" "),n("el-table",{staticStyle:{width:"100%"},attrs:{data:t.tableData,border:""}},[n("el-table-column",{attrs:{type:"index",width:"50"}}),t._v(" "),n("el-table-column",{attrs:{prop:"model_number",label:"手机型号",width:"180"}}),t._v(" "),n("el-table-column",{attrs:{prop:"is_usable",label:"状态",width:"180"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v("\n        "+t._s(e.row.is_usable?"可用":"不可用")+"\n      ")]}}])}),t._v(" "),n("el-table-column",{attrs:{prop:"version",label:"系统版本"}}),t._v(" "),n("el-table-column",{attrs:{prop:"sn_number",label:"SN"}}),n("el-table-column",{attrs:{fixed:"right",label:"操作",width:"120"},scopedSlots:t._u([{key:"default",fn:function(e){return[n("el-button",{attrs:{type:"text",size:"small"},on:{click:function(n){return t.edit(e.row)}}},[t._v("\n          修改\n        ")]),t._v(" "),n("el-button",{attrs:{type:"text",size:"small"},on:{click:function(n){return t.del(e.row.id)}}},[t._v("\n          删除\n        ")])]}}])})],1),t._v(" "),n("div",{staticClass:"pagination"},[n("el-pagination",{attrs:{background:"",layout:"prev, pager, next",total:t.total},on:{"current-change":t.currentChange}})],1),t._v(" "),n("el-dialog",{attrs:{title:"修改",visible:t.dialogFormVisible},on:{"update:visible":function(e){t.dialogFormVisible=e}}},[n("el-form",{attrs:{model:t.form}},[n("el-form-item",{attrs:{label:"手机型号","label-width":t.formLabelWidth}},[n("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.model_number,callback:function(e){t.$set(t.form,"model_number",e)},expression:"form.model_number"}})],1),t._v(" "),n("el-form-item",{attrs:{label:"状态","label-width":t.formLabelWidth}},[n("el-switch",{attrs:{"active-color":"#13ce66"},model:{value:t.form.is_usable,callback:function(e){t.$set(t.form,"is_usable",e)},expression:"form.is_usable"}})],1),t._v(" "),n("el-form-item",{attrs:{label:"系统版本","label-width":t.formLabelWidth}},[n("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.version,callback:function(e){t.$set(t.form,"version",e)},expression:"form.version"}})],1),t._v(" "),n("el-form-item",{attrs:{label:"SN","label-width":t.formLabelWidth}},[n("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.sn_number,callback:function(e){t.$set(t.form,"sn_number",e)},expression:"form.sn_number"}})],1)],1),t._v(" "),n("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:function(e){t.dialogFormVisible=!1}}},[t._v("取 消")]),t._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:t.editSubmit}},[t._v("确 定")])],1)],1)],1)},staticRenderFns:[]};var L=n("VU/8")(y,k,!1,function(t){n("thQJ")},"data-v-3e33266c",null).exports;a.default.use(i.a);var S=new i.a({routes:[{path:"/",name:"index",component:L}]});n("tvR6");a.default.use(b.a),a.default.config.productionTip=!1,new a.default({el:"#app",router:S,components:{App:r},template:"<App/>"})},o8nZ:function(t,e){},thQJ:function(t,e){},tvR6:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.5bc2a66b2d9c4825ae70.js.map