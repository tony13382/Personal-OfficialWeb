from app.layouts.project import ProjectPage
from app.variables import GapSet, SpaceSet, ThemeColor
from app.elements import (
    Card,
    DivBar,
    IconBlock,
    Html,
    Image,
    LinkButton,
    ListDiv,
    ListStr,
    Text,
    UiImageCarousel,
)


page = ProjectPage(
    title="Pincake AI 履歷",
    description="Pincake 針對求職新鮮人的產品。主要產品為 AI 求職助手平台,根據求職者提供的公司職缺與工作描述等內容為用戶提供求職整合服務。",
    startdate="2023/09",
    enddate="2023/12",
    status="closed",
    colorSet=ThemeColor().red,
    prefix="pincakeAi",
    cover="/assets/imgs/projects/pincakeAi/cover.png",
    description_links=[
        LinkButton(
            content="企劃書網址",
            href="https://drive.google.com/file/d/1OlLW1L3FS_4KHjfdIIe_AVNtSnrNocFT/view?usp=sharing",
            open_in_tab=True,
            icon="bi-cloud",
        ),
    ],
    skill_types=["design", "plan"],
    tags=["介面設計", "行銷企劃"],
    children=[
        Card(
            header=UiImageCarousel(
                [
                    "/assets/imgs/projects/pincakeAi/uiHome.png",
                    "/assets/imgs/projects/pincakeAi/uiInfo.png",
                    "/assets/imgs/projects/pincakeAi/uiMeet.png",
                ]
            ),
            body=[
                ListDiv(
                    [
                        Text("AI 履歷助手", bold=True),
                        Text(
                            "透過AI生成初版高品質履歷,節省內容製作、排版與美編的時間。"
                        ),
                    ]
                ),
                DivBar(),
                ListDiv(
                    [
                        Text("AI 人物面試", bold=True),
                        Text(
                            "提供擬真人物對話面試來模擬真人面試體驗,提升面試技巧和自信心。"
                        ),
                    ]
                ),
                ListDiv(
                    [
                        IconBlock(
                            title="Figma 原型展示連結",
                            subtitle="Figma",
                            icon="bi-phone-fill",
                            src="https://www.figma.com/proto/Pl8coAJTROnRdb5HVGBieY/202312--Pincake-Design?page-id=0:1&node-id=11-194&viewport=644,710,0.08&t=QndT068SEi3PAePE-1&scaling=scale-down&content-scaling=fixed",
                        ),
                    ],
                    space=SpaceSet(mt=3),
                ),
            ],
        ),
        Card(
            header=ListDiv(
                [
                    Image(
                        "/assets/imgs/projects/pincakeAi/workflowUser.png",
                        "workflow",
                        True,
                    )
                ]
            ),
            body=[Text("系統使用流程", "h3")],
        ),
        Card(
            body=[
                Text("市場分析", "h3"),
                Text(
                    "根據 104 徵才資料庫數據 2023 年職缺比 2020 年大幅成長成長 94%，僅一家人力銀行職缺需求數量就高達 56 萬。除此之外根據 2023 年的《The Future of Jobs Report》，全球預計將出現至少 60 億個就業機會，其中某些領域的就業增長率預計將達到 10% 以上。這表明不只是台灣需求成長，國際人才市場的發展也呈現穩健增長，而履歷製作的相關服務也會因此受惠。"
                ),
                DivBar(),
                Text("求職相關的產品市場主要分為三類"),
                ListStr(
                    [
                        "`線上履歷製作工具`：這些工具提供多種履歷模板和自訂功能，讓使用者能輕鬆地製作符合其需求的履歷。常見的線上履歷製作工具包括：Canva、Visual CV、CakeResume。自 2023 年開始觀察，根據 CakeResume 公開的用戶數據，至少在台有 200 萬使用者使用了這類服務，且這一市場仍在持續擴大。",
                        "`履歷分析工具`：這些工具利用人工智慧或機器學習技術來分析履歷內容，並提供建議，有助於使用者提升履歷品質。常見的履歷分析工具包括：履歷診斷 - 104 人力銀行、履歷診斷 - 1111 人力銀行。自 2023 年開始觀察，根據 104 人力銀行和 1111 人力銀行公開的用戶數據，至少有 10 萬名使用者使用了這類服務，並為之付費優化自己的履歷。",
                        "`AI 模擬面試`：大多數模擬面試的服務多是以真人的服務進行，且大多都是針對外商或國外求職、求學進行專人的服務。並且在台灣只有像是原本履歷投遞平台人力銀行有類似的服務。",
                    ]
                ),
            ]
        ),
        Card(
            body=[
                Text("STP 分析", "h3"),
                Text("Segmentation：求職平台市場區隔", bold=True),
                Html(
                    """
<table class="table" style="margin: 0rem -0.5rem;">
    <tbody>
        <tr>
            <td>教育階段</td>
            <td>大學生 / 碩士研究生 / 博士生</td>
        </tr>
        <tr>
            <td>就業狀況</td>
            <td>在學實習之學生、剛畢業之社會新鮮人、在職並計畫轉職者、自由職業者或失業者</td>
        </tr>
        <tr>
            <td>產業類別</td>
            <td>不拘/新創/外商/中高階</td>
        </tr>
        <tr>
            <td>年齡區間</td>
            <td>20～25 / 26～30 / 31～35 / 36～40</td>
        </tr>
        <tr>
            <td>平台重點功能</td>
            <td>刊登職缺 / 履歷製作 / 專業社群平台 / 面試模擬</td>
        </tr>
    </tbody>
</table>
"""
                ),
                Text(
                    "Targeting：台灣 20～30 剛從大學或碩士畢業計畫申請職缺的社會新鮮人",
                    bold=True,
                ),
                Html(
                    """
<table class="table" style="margin: 0rem -0.5rem;">
    <tbody>
        <tr>
            <td>群體痛點</td>
            <td>社會新鮮人往往缺乏職場經驗，對於企業所期待的面試表現及履歷掌握度不高，這個族群處於社群平台的時間較其他年齡層高，容易感到焦慮及社恐的比例也相對較高。
            </td>
        </tr>
        <tr>
            <td>最常使用的產品特色</td>
            <td>高CP值的：希望能不花大錢又高效率達成目標、簡易又好操作的、能保障個人隱私需求的、客製化且能提供個性化的專業建議及服務。</td>
        </tr>
        <tr>
            <td>資訊蒐集方式</td>
            <td>各大社群平台、同儕。</td>
        </tr>
        <tr>
            <td>收入</td>
            <td>剛畢業的求職階段，金流多仍來自父母或實習打工，收入普遍不高。</td>
        </tr>
        <tr>
            <td>使用產品 / 服務的動機</td>
            <td>開始計畫未來職涯方向時身邊同儕都在投遞履歷 。</td>
        </tr>
        <tr>
            <td>購買產品 / 服務的動機 時間、地點（實體或網路通路）和付款方</td>
            <td>獲得產品價值並渴望更高階功能、網路通路、線上支付工具。</td>
        </tr>
    </tbody>
</table>
"""
                ),
                Text(
                    "Positioning：讓求職者能夠進行專業模擬面試的求職平台。", bold=True
                ),
                ListDiv(
                    [
                        Text(
                            "求職者在求職前能夠依據應徵企業及職位需求，能獲得AI擬真面試並針對目標職缺提供專業建議，以解決求職者在初次面試前龐大的不確定性及焦慮感。"
                        ),
                        Text(
                            "使用者為職場年輕人，提供智慧生成解決給初入不知道從何開始的心理，透過擬真面試情境及客製化專業履歷生成;平時就可以於我們的平台分享自己經驗內容（符合這一層族群），只要點選想應徵的職位，系統即直接根據分享的內容篩選完成自動化生成客製化履歷。"
                        ),
                        Text(
                            "我們對於求職輔助工具市場的競爭策略主要是大量結合人工智慧、文本分析技術並利用流暢且低操作的方式為客戶提供彈性、簡易有效的求職體驗，讓求職的過程可以成為輕鬆且直覺呈現自我價值的過程，而非是一件令人心力交瘁、整理繁雜資料又陷入焦慮不安的一項挑戰。"
                        ),
                    ]
                ),
            ],
            body_gap=GapSet("large"),
        ),
        Card(
            body=[
                Text("SWOT", "h3"),
                Text("Strengths", bold=True),
                ListStr(
                    [
                        "專注模擬面試服務：作為市場上少數專注於模擬面試的平台，可以提供獨特價值給求職者，解決面試過程中的準備和不確定性問題。",
                        "智慧生成解決方案：利用人工智慧和文本分析技術，提供客製化、智慧生成的履歷，降低求職者的操作成本，簡化求職流程。",
                        "團隊成員背景多元且年輕，有機會更好地理解目標族群需求。",
                    ]
                ),
                Text("Weaknesses", bold=True),
                ListStr(
                    [
                        "草創初期，品牌知名度不足，需要加強市場宣傳和推廣。",
                        "產品原型尚未開發成熟，可能面臨使用者體驗上的挑戰。",
                        "提供履歷撰寫建議的專業度待確認，需要不斷優化以提高客戶滿意度。",
                    ]
                ),
                Text("Opportunities", bold=True),
                ListStr(
                    [
                        "擁抱人工智慧趨勢：利用人工智慧技術持續優化模擬面試和履歷生成服務，以滿足不斷變化的市場需求。",
                        "年輕族群定位： 面向職場年輕人，符合當今求職市場的主要使用者群體，有機會建立品牌忠誠度。",
                        "求職市場競爭度越來越大，客製化面試建議及需求提升，可不斷提升產品的價值。",
                        "面對現今社恐比例攀升的現象，提供虛擬模擬面試服務，使用者能在安全、無壓力的環境中模擬真實面試情境，降低焦慮感。",
                    ]
                ),
                Text("Threats", bold=True),
                ListStr(
                    [
                        "現有競爭對手眾多，市場變動快速，需要不斷創新以保持競爭力。",
                        "用戶資訊的隱私和安全問題可能成為潛在風險，需要嚴格保護用戶數據以建立信任。",
                    ]
                ),
            ]
        ),
    ],
)
