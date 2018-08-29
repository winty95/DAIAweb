# DAIAweb
<p>본 웹사이트는 인공지능을 공부하는 동국대학교 학회 DAIA의 웹페이지입니다.</p>
<p>DAIA(동국대학교 인공지능 학생협회)는 인공지능과 관련하여 스터디, 세미나, 토론, 연구등을 진행하기 위한 교내 학회입니다.</p>
<p>2018년 1월 설립되었고, 한 학기를 기준으로 기수별로 운영되며, 컴퓨터공학, 전자전기공학, 수학 등 다양한 전공의 학생들로 구성되어있습니다.</p>
<p>저희 학회는 시각처리, 자연어처리, 음성신호 처리등 다양한 도메인에 대한 기존, 최신의 딥러닝 기법들을 공부합니다.</p>
<hr>    
#프로젝트 설명(180820 기준)
<p>웹사이트 개발은 2018년 여름학기(8월)부터 시작되었습니다. 한선웅 회원은 7월에 Newbi 과정에서 Django 수업을 담당하였기에 다른 회원들보다 익숙하다는 판단하, 개발을 총괄담당하였습니다. 여현웅, 김선우, 김형규, 안지훈, 권성호 회원과 함께 개발하였습니다.</p>
<p>웹사이트에 사용된 DB는 강수현 회원이 초안을 설계하였으며 이후 개발에서 필요에 따라 약간씩 변경하였습니다.</p>
<p>AWS 서버에 올리는 작업은 노준형 회원이 할 예정입니다.</p>
<p>학회 소개글은 기장인 전용진 회원이 작성해주셨습니다.</p>
<hr>  
<p>구체적으로 행한 태스크는 다음과 같습니다.</p>
<p>한선웅 : 각자의 코드를 통합 - 크게 3가지(게시판, 관리자, 로그인)앱으로 모듈화하고 DB 수정 및 연결, 기능만 구현된 각 페이지에 프론트입히기, 메인페이지에 최신글4개 노출 구현, 앨범게시판에서 앨범게시판에서 사진이 2장이상일경우 1장만 보이도록 구현 with image multiple upload, 멤버 소개탭에서 여러 기수에 해당할 경우 처리 구현, 처리가능한 모든 url에 로그인정보 부여하여 비정상적인 접근 방지, 게시판에 글쓰기/수정/삭제 권한 부여, 그 외 기타 잔업..<br>
<br>
여현웅 : 웹페이지의 디자인 제안 - 기초적인 HTML 템플릿 틀 제공(<a href="https://startbootstrap.com/template-overviews/modern-business/" rel="nofollow">https://startbootstrap.com/template-overviews/modern-business/</a> 수정), Member 게시판의 modal form으로 세련된 멤버 소개탭 구축 - 기수별 전환탭 구현<br>
<br>
김선우 : 로그인/로그아웃, 회원가입 구현(request.session 이용) - 로그인 정보의 활용 설명<br>
<br>
김형규, 안지훈 : 관리자 페이지 구현 - 회원가입요청 처리와 회원정보 수정<br>
<br>
권성호 : Member게시판 보조, 통합과정에서 상이한 DB 필드 교체작업 수행<br>
<br></p>
<p>총괄담당자로서 짧게 소감을 쓰고 프로젝트 설명을 마치겠습니다.</p>
<ul>
<li>프로젝트가 끝나고 웹사이트가 제대로 돌아가는걸 확인하고 쓸 예정 -</li>
