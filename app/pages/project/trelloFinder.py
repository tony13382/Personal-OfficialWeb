from app.layouts.project import ProjectPage
from app.variables import ThemeColor
from app.elements import (
    AccordionBlock,
    AccordionItem,
    Canva,
    Card,
    Div,
    DivBar,
    IconBlock,
    Html,
    Image,
    LinkButton,
    ListDiv,
    Score,
    Text,
    Tool,
)


page = ProjectPage(
    title="Trello 知識小幫手 2.0",
    description="[作品＆論文] 在 Trello 平台結合大型語言模型協助學生進行自主學習資源搜索與互動。",
    subdescription="擔任：教育系統 RD 工程師<br>負責：軟體架構設計、API 設計、資料庫設計、軟體開發",
    startdate="2023/07",
    enddate="2024/07",
    status="running",
    colorSet=ThemeColor().blue,
    prefix="trelloFinder",
    cover="/assets/imgs/projects/trelloFinder/cover.png",
    tags=[
        "文本探勘",
        "文本搜尋算法",
        "大型語言模型",
        "向量資料管理",
        "APIs 設計",
        "佇列系統",
    ],
    description_links=[
        LinkButton(
            content="專案網址",
            href="https://github.com/tony13382/Tools-TrelloFinderV2",
            icon="bi-github",
            open_in_tab=True,
        ),
    ],
    scores=[
        Score(
            name="TWELF 2024 第十九屆台灣數位學習發展研討會",
            group="AIES 組",
            score="最佳論文獎",
        )
    ],
    tools=[
        Tool("Flask", "Webhook APIs 建立"),
        Tool("RabbitMQ", "建立任務佇列處理系統，處理大量用戶請求時不會造成服務阻塞"),
        Tool("MongoDB", "主要系統資料庫，紀錄所有學生互動資料"),
        Tool("Milvus", "系統知識向量資料庫，用於建置與管理 RAG 知識搜尋"),
        Tool("Sentence-BERT", "文本向量化技術、模型訓練與微調"),
    ],
    children=[
        Card(
            header=Canva(
                src="https://www.canva.com/design/DAGAH5TIfcM/noA5DlVGa0eP-raZZdv56w/view?embed"
            ),
            body=[Text("系統使用說明", "h3")],
        ),
        Card(
            header=Image(
                src="/assets/imgs/projects/trelloFinder/workflowPerpareData.png",
                alt="知識文本資料前處理流程",
                allow_pop=True,
            ),
            body=[
                Text("知識文本資料前處理", "h3"),
                DivBar(),
                Text(
                    "取得文章的標題、內文與連結後會以純文本的形式儲存至 mongoDB 的文章文本資料庫進行管理，為了滿足 RAG 的文章搜尋需求，標題與內文會合併成索引文本，索引文本會在透過 Sentence-BERT 的 paraphrase-multilingual-mpnet-base-v2 多語言模型轉換成固定長度的向量並儲存至文章向量資料庫。"
                ),
            ],
        ),
        Card(
            header=Image(
                src="/assets/imgs/projects/trelloFinder/workflowModule.png",
                alt="模組建立流程",
                allow_pop=True,
            ),
            body=[
                Text("模組建立", "h3"),
                DivBar(),
                Text("搜索架構", bold=True),
                Text(
                    "融合 BM25（詞頻）、TF-IDF、共現分析 與 SBERT Embeding 技術打造的資源推薦算法，透過使用者輸入的關鍵字，進行科普資源搜尋。"
                ),
                DivBar(),
                Text("回應架構", bold=True),
                Text(
                    "基於 RAG 與鏈式提示策略設計，使用大型語言模型（GPT-4 Turbo）生成適切的回應與延伸提問。"
                ),
            ],
            body_gap_size="small",
        ),
        Card(
            header=Image(
                src="/assets/imgs/projects/trelloFinder/workflowTrello.png",
                alt="Trello 資料建立流程",
                allow_pop=True,
            ),
            body=[
                Text("Trello 資料建立流程", "h3"),
            ],
        ),
        Card(
            body=[
                Text("提示詞列表", "h3"),
                AccordionBlock(
                    items=[
                        AccordionItem(
                            title="萃取提示詞・基於 GPT 3.5、溫度設定為 0",
                            items=[
                                Html(
                                    """
<table class="table">
    <thead>
        <tr>
            <th scope="col">role</th>
            <th scope="col">prompt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>system</td>
            <td>#zh_tw 你是一位使用繁體中文的自然科學中學老師，正在跟剛接觸研究領域的學生交談，首先學生正在研究
                <span class="text-theme fw-bold">研究主題</span>，而你需要幫助學生瞭解相關知識，因此你需要生成回答並追問學生讓學生回答以促進學生對
                <span class="text-theme fw-bold">研究主題</span>
                深度思考。輸出的文本需要基於 Markdown 語法。
            </td>
        </tr>
        <tr>
            <td>user</td>
            <td>*聊天文本（舊～新）*</td>
        </tr>
    </tbody>
</table>
"""
                                ),
                            ],
                            expanded=True,
                        ),
                        AccordionItem(
                            title="回應提示詞・基於 GPT 4 turbo、溫度設定為 0.1",
                            items=[
                                Text("生成回應", bold=True),
                                Html(
                                    """
<table class="table">
    <thead>
        <tr>
            <th scope="col">role</th>
            <th scope="col">prompt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>system</td>
            <td>#zh_tw 你是一位使用繁體中文的自然科學中學老師，正在跟剛接觸研究領域的學生交談，首先學生正在研究
                <span class="text-theme fw-bold">研究主題</span>
                而你需要幫助學生瞭解相關知識，因此你需要1.
                基於參考資料嘗試回答學生的問題，並在回答之中強制標注[文章編號]。2.
                如果參考資料無法解答問題則只告知現有資料無法回答問題。3. 根據對話紀錄生成回應。輸出的文本需要基於
                Markdown 語法。
            </td>
        </tr>
        <tr>
            <td>assistant</td>
            <td>以下是我們給付的參考資料：以 JSON 格式呈現，格式如下｛article_id: 文章編號,content :
                文章的實際內容｝\n <span class="text-theme fw-bold">文章內容</span></td>
        </tr>
        <tr>
            <td>user</td>
            <td><span class="text-theme fw-bold">聊天文本（舊～新）</span>
            </td>
        </tr>
    </tbody>
</table>
"""
                                ),
                                Text("生成反問", bold=True),
                                Html(
                                    """
<table class="table">
    <thead>
        <tr>
            <th scope="col">role</th>
            <th scope="col">prompt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>system</td>
            <td>#zh_tw 你是一位使用繁體中文的自然科學中學老師正在跟剛接觸研究領域的學生交談，首先學生正在研究 <span class="text-theme fw-bold">研究主題</span>，而你需要幫助學生瞭解相關知識，因此你需要基於以下聊天內容提出問題給學生讓學生回答以促進學生對
                <span class="text-theme fw-bold">研究主題</span>
                深度思考。輸出的文本只需要問題無需標題，使用 Markdown 語法輸出。
            </td>
        </tr>
        <tr>
            <td>assistant</td>
            <td>以下是我們給付的參考資料：以 JSON 格式呈現，格式如下｛article_id: 文章編號,content :
                文章的實際內容｝\n <span class="text-theme fw-bold">文章內容</span></td>
        </tr>
        <tr>
            <td>user</td>
            <td><span class="text-theme fw-bold">聊天文本（舊～新）</span>
            </td>
        </tr>
        <tr>
            <td>assistant</td>
            <td><span class="text-theme fw-bold">對話回應文本（上表的結果）</span>
            </td>
        </tr>
        <tr>
            <td>user</td>
            <td>請根據上述內容撰寫問題給學生，促進學生思考。</td>
        </tr>
    </tbody>
</table>
"""
                                ),
                            ],
                        ),
                    ]
                ),
            ],
            body_gap_size="large",
        ),
        Card(
            body=[
                Text("回應模組資料前處理", "h3"),
                DivBar(),
                Text("聊天文本處理", bold=True),
                Image(
                    "/assets/imgs/projects/trelloFinder/workflowPrepareChat.png",
                    "聊天文本處理流程",
                    allow_pop=True,
                ),
                DivBar(),
                Text("知識文本處理", bold=True),
                Image(
                    "/assets/imgs/projects/trelloFinder/workflowPrepareKnow.png",
                    "知識文本處理流程",
                    allow_pop=True,
                ),
            ]
        ),
        Card(
            header=Canva(
                "https://www.canva.com/design/DAF27I-RV30/bVeemVpl-SsdQANIouLtIg/view?embed"
            ),
            body=[
                Div(Text("搜尋模組", "span")),
                Text("使用自然語言技術建構自主學習資源推薦系統", "h3"),
                Text(
                    "融合 BM25（詞頻）、TF-IDF、SBERT Embeding 技術打造的資源推薦算法，透過使用者輸入的關鍵字，進行科普資源搜尋。"
                ),
                ListDiv(
                    [
                        IconBlock(
                            src="https://www.canva.com/design/DAF27I-RV30/bVeemVpl-SsdQANIouLtIg/view",
                            icon="bi-file-earmark-ppt",
                            title="研究會議簡報連結",
                            subtitle="Canva",
                        ),
                        IconBlock(
                            src="https://drive.google.com/file/d/10Oz-daozOXayrbwCAk7b9xX1EqEm5nYF/view?usp=drivesdk",
                            icon="bi-file-earmark-arrow-down",
                            title="研討會論文文件",
                            subtitle="PDF",
                        ),
                    ],
                    mt=2,
                ),
            ],
        ),
        Card(
            header=Canva(
                "https://www.canva.com/design/DAGKAc57KAs/XCcrwiCGLdZ5_E4Wz3-Reg/view?embed"
            ),
            body=[
                Div(Text("生成模組", "span")),
                Text("在自主學習環境比較不同提示策略對大型語言模型回應的影響", "h3"),
                Text(
                    "基於 RAG 與鏈式提示策略，進行大型語言模型回應的生成模組，並進行實驗比較不同提示策略對回應的影響。"
                ),
                ListDiv(
                    [
                        IconBlock(
                            src="https://drive.google.com/file/d/1xoYvRgNZ3Li3kEbwFW5QEBuK-JOLogfz/view",
                            icon="bi-file-earmark-ppt",
                            title="研究會議簡報連結",
                            subtitle="Canva",
                        ),
                        IconBlock(
                            src="https://drive.google.com/file/d/1y7yCt21CVPbaPbOCFheRRoO3R98cCWuP/view?usp=sharing",
                            icon="bi-file-earmark-arrow-down",
                            title="研討會論文文件",
                            subtitle="PDF",
                        ),
                    ],
                    mt=2,
                ),
            ],
        ),
    ],
)
